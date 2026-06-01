
---

## StarCraft-Battle-Outcome-Simulator

```md
# StarCraft Battle Outcome Simulator

Python 객체지향 프로그래밍을 활용하여 StarCraft 스타일의 유닛 전투 흐름을 시뮬레이션하는 프로젝트입니다.

## Project Overview

본 프로젝트는 StarCraft 유닛을 Python 클래스로 모델링하고, 유닛 생성, 이동, 공격, 스킬 사용, 피해 처리 과정을 구현한 전투 시뮬레이션입니다.  
실제 2D 게임 화면을 구현하는 프로젝트가 아니라, 객체지향 구조를 기반으로 전투 결과와 유닛 동작 흐름을 콘솔 출력으로 확인하는 프로젝트입니다.

## Features

- Unit 클래스 기반 일반 유닛 모델링
- AttackUnit 상속 구조 구현
- 지상 유닛과 공중 유닛 이동 방식 분리
- Marine 스팀팩 기능 구현
- Tank 시즈모드 기능 구현
- Wraith 클로킹 기능 구현
- 랜덤 피해량 기반 전투 결과 처리
- Python class, inheritance, method overriding 학습 코드 포함

## Tech Stack

- Python
- Object-Oriented Programming
- Class / Instance
- Inheritance
- Method Overriding
- Random Module

## Directory Structure

```text
StarCraft-Battle-Outcome-Simulator/
│
├─ src/
│   ├─ starcraft_simulation_main.py
│   ├─ attack_unit.py
│   └─ flyable_unit.py
│
├─ examples/
│   ├─ unit_class_basic.py
│   ├─ unit_method_practice.py
│   ├─ method_overriding_practice.py
│   ├─ inheritance_practice.py
│   ├─ super_practice_1.py
│   └─ super_practice_2.py
│
├─ practice/
│   ├─ pass_statement_practice.py
│   └─ python_oop_practice.py
│
└─ README.md
