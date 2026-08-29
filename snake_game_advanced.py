"""
Snake Game - Rắn Săn Mồi
Advanced Version with Sound and Better Graphics
"""

import pygame
import random
import sys
from enum import Enum
from dataclasses import dataclass

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GRAY = (128, 128, 128)

# Game speed
FPS = 10

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

@dataclass
class GameStats:
    score: int = 0
    level: int = 1
    game_over: bool = False
    paused: bool = False
    high_score: int = 0

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("🐍 Rắn Săn Mồi - Snake Game")
        self.clock = pygame.time.Clock()
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_large = pygame.font.Font(None, 72)
        
        self.stats = GameStats()
        self.load_high_score()
        self.reset_game()
    
    def load_high_score(self):
        """Load high score from file if exists"""
        try:
            with open("highscore.txt", "r") as f:
                self.stats.high_score = int(f.read())
        except FileNotFoundError:
            self.stats.high_score = 0
    
    def save_high_score(self):
        """Save high score to file"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            with open("highscore.txt", "w") as f:
                f.write(str(self.stats.high_score))
    
    def reset_game(self):
        """Reset game state"""
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.stats.score = 0
        self.stats.game_over = False
        self.stats.paused = False
        self.stats.level = 1
    
    def spawn_food(self):
        """Generate food at random location not occupied by snake"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def handle_events(self):
        """Handle user input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                # Direction controls
                if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.next_direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.next_direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.next_direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.next_direction = Direction.RIGHT
                
                # Game controls
                elif event.key == pygame.K_SPACE:
                    if self.stats.game_over:
                        self.reset_game()
                    else:
                        self.stats.paused = not self.stats.paused
                elif event.key == pygame.K_ESCAPE:
                    return False
        
        return True
    
    def update(self):
        """Update game state"""
        if self.stats.game_over or self.stats.paused:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.stats.game_over = True
            self.save_high_score()
            return
        
        # Check self collision
        if new_head in self.snake:
            self.stats.game_over = True
            self.save_high_score()
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.stats.score += 10
            self.stats.level = 1 + self.stats.score // 100
            self.food = self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw_game(self):
        """Draw game elements"""
        # Draw snake
        for i, segment in enumerate(self.snake):
            rect = pygame.Rect(segment[0] * GRID_SIZE + 1, segment[1] * GRID_SIZE + 1, 
                             GRID_SIZE - 2, GRID_SIZE - 2)
            
            # Head is brighter
            if i == 0:
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
                pygame.draw.circle(self.screen, YELLOW, 
                                 (segment[0] * GRID_SIZE + GRID_SIZE // 2,
                                  segment[1] * GRID_SIZE + GRID_SIZE // 2), 3)
            else:
                pygame.draw.rect(self.screen, GREEN, rect)
        
        # Draw food
        food_rect = pygame.Rect(self.food[0] * GRID_SIZE + 1, 
                               self.food[1] * GRID_SIZE + 1,
                               GRID_SIZE - 2, GRID_SIZE - 2)
        pygame.draw.ellipse(self.screen, RED, food_rect)
    
    def draw_ui(self):
        """Draw UI elements"""
        # Score panel background
        pygame.draw.rect(self.screen, GRAY, (0, 0, WINDOW_WIDTH, 50))
        pygame.draw.line(self.screen, WHITE, (0, 50), (WINDOW_WIDTH, 50), 2)
        
        # Score text
        score_text = self.font_medium.render(f"Score: {self.stats.score}", True, YELLOW)
        level_text = self.font_medium.render(f"Level: {self.stats.level}", True, BLUE)
        high_score_text = self.font_small.render(f"High: {self.stats.high_score}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (WINDOW_WIDTH // 2 - 60, 10))
        self.screen.blit(high_score_text, (WINDOW_WIDTH - 150, 15))
    
    def draw_pause_screen(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_large.render("PAUSED", True, YELLOW)
        resume_text = self.font_medium.render("Press SPACE to resume", True, WHITE)
        
        pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        resume_rect = resume_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        
        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(resume_text, resume_rect)
    
    def draw_game_over_screen(self):
        """Draw game over overlay"""
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        score_text = self.font_medium.render(f"Final Score: {self.stats.score}", True, YELLOW)
        high_score_text = self.font_medium.render(f"High Score: {self.stats.high_score}", True, BLUE)
        restart_text = self.font_small.render("Press SPACE to restart or ESC to quit", True, WHITE)
        
        y_offset = WINDOW_HEIGHT // 2 - 100
        self.screen.blit(game_over_text, 
                        game_over_text.get_rect(center=(WINDOW_WIDTH // 2, y_offset)))
        self.screen.blit(score_text, 
                        score_text.get_rect(center=(WINDOW_WIDTH // 2, y_offset + 70)))
        self.screen.blit(high_score_text, 
                        high_score_text.get_rect(center=(WINDOW_WIDTH // 2, y_offset + 120)))
        self.screen.blit(restart_text, 
                        restart_text.get_rect(center=(WINDOW_WIDTH // 2, y_offset + 180)))
    
    def draw(self):
        """Render all game elements"""
        self.screen.fill(BLACK)
        
        # Draw grid
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (30, 30, 30), (x, 50), (x, WINDOW_HEIGHT), 1)
        for y in range(50, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (30, 30, 30), (0, y), (WINDOW_WIDTH, y), 1)
        
        # Draw game area border
        pygame.draw.rect(self.screen, WHITE, (0, 50, WINDOW_WIDTH, WINDOW_HEIGHT - 50), 2)
        
        # Draw game elements
        self.draw_game()
        self.draw_ui()
        
        # Draw overlays
        if self.stats.paused:
            self.draw_pause_screen()
        elif self.stats.game_over:
            self.draw_game_over_screen()
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()