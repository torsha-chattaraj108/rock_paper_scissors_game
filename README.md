# Algorithmic Rock-Paper-Scissors (RPS) Engine

A production-grade Python CLI application featuring an intelligent backend engine that implements predictive analytics and dynamic difficulty scaling. Unlike standard random-choice implementations, this system features a predictive heuristics engine that analyzes user historical data to actively counter player strategies in real time.

## 🚀 Key Features

* **Advanced Architecture**: Strict separation of concerns divided into a core computational engine, application entry lifecycle, and automated test suite.
* **Predictive Heuristics (Difficult Mode)**: Tracks and analyzes historical user move frequencies to dynamically forecast and counter subsequent player actions.
* **Dynamic Session Management**: Supports user-defined match session lengths with persistent memory allocation across the lifecycle of the session.
* **Real-Time Analytics Engine**: Dynamically calculates rolling win/loss/tie ratios, performance percentages, and consecutive victory/defeat streaks.
* **Deterministic Unit Testing**: High-coverage test suite ensuring logic reliability across all core game loops, streak counters, and predictive branches.

## 🏗️ System Architecture

The project is structured following modular engineering patterns to maximize maintainability and testability:

```text
├── main.py          # Application entry point, user input loop, and CLI state manager
├── engine.py        # Core business logic, pattern analysis, and analytics calculations
└── test_engine.py   # Automated unit test cases validating core algorithmic accuracy
```

## 🛠️ Technical Stack

* **Language**: Python 3.x
* **Testing Framework**: PyTest / Unittest (Standard Library)
* **Libraries**: Python Core Collections (State tracking & history logging)

## 📦 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com
   cd algorithmic-rps-engine
   ```

2. **Run the Application**
   ```bash
   python main.py
   ```

3. **Execute Automated Tests**
   ```bash
   python -m unittest test_engine.py
   ```

## 🧠 Core Algorithmic Logic

### Easy Mode
Utilizes standard pseudo-random distribution (`random.choice`) giving the AI an even 33.3% probability split per move.

### Difficult Mode (Predictive Analytics)
The backend maintains a sequential history ledger of the player's choices. The heuristic engine processes the frequency of past moves within the active session to evaluate behavioral bias:
$$\text{Move Probability} = \frac{\text{Count of Specific Move}}{\text{Total Session Moves Played}}$$
The engine identifies the user's statistically favored choice and deploys the absolute counter-move, elevating the AI's efficiency over prolonged sessions.

## 📈 Planned Future Enhancements
* Transition local logic into a high-performance **FastAPI** web endpoint (`POST /api/v1/play`).
* Integrate a relational **PostgreSQL** database to persist historical player metrics across multiple sessions.
* Introduce a distributed caching layer (**Redis**) for real-time multiplayer session state tracking.
