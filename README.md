# 🎮 RPG Combat Simulator

A fully featured **turn-based RPG Combat Simulator** built in Python to demonstrate core **Object-Oriented Programming (OOP)** principles.

This project showcases **Inheritance**, **Polymorphism**, **Encapsulation**, and **Abstraction** through a clean, modular architecture with 17+ classes, a functional GUI, and persistent save/load system.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

- **Rich Character System** — Play as Warrior, Mage, or Archer with unique combat styles
- **Interactive GUI** — Built with Tkinter for smooth user experience
- **Real-time Combat Log** — Watch every attack, damage, and event unfold
- **Inventory & Items** — Weapons, Armor, and Potions with full management
- **Save & Load System** — Persist your character progress using JSON
- **Polymorphic Combat** — Different attack behaviors per character class
- **Turn-based Battles** — Fight against Goblins and powerful Boss enemies

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** — For the graphical user interface
- **JSON** — For data persistence (save/load)
- **Mermaid** — For architecture diagrams in documentation

---

## 📋 Project Structure

```bash
rpg-combat-simulator/
├── main.py                 # Entry point - Launches the GUI
├── characters/
│   ├── base_entity.py
│   ├── character.py
│   ├── player.py
│   ├── enemy.py
│   ├── warrior.py
│   ├── mage.py
│   ├── archer.py
│   ├── goblin.py
│   └── boss.py
├── items/
│   ├── item.py
│   ├── weapon.py
│   ├── armor.py
│   ├── potion.py
│   └── inventory.py
├── combat/
│   └── combat_engine.py
├── utils/
│   └── save_load_manager.py
├── ui/
│   └── game_ui.py
├── data/                   # JSON save files will be stored here
├── diagrams/               # UML diagrams (optional)
└── README.md
