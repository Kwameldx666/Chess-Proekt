
# 🏆 Chess AI Project / Шахматный ИИ Проект

<div align="center">

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/pygame-2.0+-green.svg)](https://www.pygame.org/)
[![Chess](https://img.shields.io/badge/python--chess-1.999-orange.svg)](https://pypi.org/project/python-chess/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*An advanced chess AI implementation with multiple algorithms and interactive gameplay*

*Продвинутая реализация шахматного ИИ с множественными алгоритмами и интерактивным геймплеем*

</div>

## 🎯 Overview / Обзор

This project is a comprehensive chess AI implementation featuring multiple sophisticated algorithms for intelligent gameplay. Built with Python and Pygame, it offers an interactive chess experience where players can compete against various AI opponents with different playing styles and difficulty levels.

*Этот проект представляет собой комплексную реализацию шахматного ИИ с множественными сложными алгоритмами для интеллектуального геймплея. Построенный на Python и Pygame, он предлагает интерактивный шахматный опыт, где игроки могут соревноваться с различными ИИ-противниками с разными стилями игры и уровнями сложности.*

## ✨ Features / Функции

### 🎮 Gameplay Features
- **Interactive GUI** - Beautiful pygame-based chess interface
- **Color Selection** - Choose to play as White or Black pieces  
- **Multiple Game Modes** - Human vs AI, AI vs AI
- **Move Validation** - Automatic prevention of invalid moves
- **Real-time Board Updates** - Smooth visual feedback for all moves

### 🤖 AI Algorithms

| Algorithm | Description | Strength |
|-----------|-------------|----------|
| **MiniMax with Alpha-Beta Pruning** | Classic game theory algorithm with optimization | ⭐⭐⭐⭐⭐ |
| **Monte Carlo Tree Search (MCTS)** | Modern probabilistic search algorithm | ⭐⭐⭐⭐ |
| **Greedy Algorithm** | Fast heuristic-based move selection | ⭐⭐⭐ |
| **Random Player** | Baseline random move generation | ⭐ |

### 🧠 Advanced Features
- **Configurable Search Depth** - Adjust AI thinking depth (up to 6 moves ahead)
- **Position Evaluation** - Sophisticated board state assessment
- **Piece Development Analysis** - Strategic piece positioning evaluation
- **Late Game Detection** - Adaptive strategy for endgame scenarios
- **Material Balance Calculation** - Precise piece value assessment

## 🚀 Quick Start / Быстрый старт

### Prerequisites / Требования
- Python 3.7 or higher
- pip package manager

### Installation / Установка

1. **Clone the repository / Клонировать репозиторий:**
   ```bash
   git clone https://github.com/Kwameldx666/Chess-Proekt.git
   cd Chess-Proekt
   ```

2. **Install dependencies / Установить зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game / Запустить игру:**
   ```bash
   python Main.py
   ```

## 🎮 How to Play / Как играть

1. **Launch the game** and select your color (White/Black)
2. **Choose your opponent** from the AI selection menu:
   - Bot 1: MiniMax with Alpha-Beta Pruning
   - Bot 2: Alternative algorithms (Greedy, MCTS, Random)
3. **Make moves** by clicking on pieces and target squares
4. **Enjoy** strategic gameplay against intelligent AI opponents!

*1. **Запустите игру** и выберите свой цвет (Белые/Черные)*
*2. **Выберите противника** из меню выбора ИИ*
*3. **Делайте ходы** кликая по фигурам и целевым клеткам*
*4. **Наслаждайтесь** стратегическим геймплеем против умных ИИ-противников!*

## 🏗️ Project Structure / Структура проекта

```
Chess-Proekt/
├── Main.py                      # Main game entry point / Главная точка входа
├── Board.py                     # GUI and board display / Интерфейс и отображение доски
├── MiniMax.py                   # MiniMax algorithm implementation
├── MCTS.py                      # Monte Carlo Tree Search algorithm
├── Evaluation.py                # Board position evaluation system
├── greedy.py                    # Greedy algorithm implementation
├── Random.py                    # Random move generation
├── PionPioneer.py              # Pioneer pawn algorithm
├── Piece_Development_Values.py  # Piece positioning values
├── requirements.txt             # Project dependencies
└── README.md                   # Project documentation
```

## 🧮 Algorithms Explained / Объяснение алгоритмов

### MiniMax with Alpha-Beta Pruning
The core algorithm uses game theory principles to find optimal moves by:
- **Maximizing** player advantage while **minimizing** opponent opportunities
- **Alpha-Beta pruning** eliminates obviously poor branches, improving performance
- **Configurable depth** allows trading speed for strategic thinking depth

### Monte Carlo Tree Search (MCTS)
A modern probabilistic approach that:
- **Simulates** thousands of random game continuations
- **Selects** moves based on statistical success rates
- **Adapts** strategy based on position characteristics

### Evaluation Function
Sophisticated position assessment considering:
- **Material balance** (piece values: Pawn=1, Knight/Bishop=3, Rook=5, Queen=9)
- **Piece development** and positioning
- **King safety** and endgame factors
- **Strategic considerations** like center control

## 🎯 Performance / Производительность

- **Search Depth**: Up to 6 moves ahead
- **Evaluation Speed**: ~10 seconds per move (configurable)
- **Move Generation**: Instant legal move validation
- **AI Response Time**: 1-10 seconds depending on complexity

## 🛠️ Development / Разработка

### Key Classes / Основные классы

- `DisplayBoard`: Handles GUI rendering and user interaction
- `Evaluation`: Implements position evaluation logic  
- `minimax()`: Core MiniMax algorithm with Alpha-Beta pruning
- `greedy_algorithm()`: Fast heuristic-based move selection

### Adding New Algorithms / Добавление новых алгоритмов

1. Create new algorithm file (e.g., `new_algorithm.py`)
2. Implement move selection function returning `chess.Move`
3. Add to opponent selection menu in `Board.py`
4. Integrate in main game loop in `Main.py`

## 🤝 Contributing / Участие в разработке

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License / Лицензия

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments / Благодарности

- [python-chess](https://python-chess.readthedocs.io/) - Excellent chess library
- [Pygame](https://www.pygame.org/) - Game development framework
- Chess AI community for algorithm insights and optimization techniques

---

<div align="center">

**Enjoy playing chess against intelligent AI! / Наслаждайтесь игрой в шахматы против умного ИИ!**

⭐ Star this repository if you found it helpful! ⭐

</div>
