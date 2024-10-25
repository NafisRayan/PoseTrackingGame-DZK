# Pose Tracking Game

This project implements a pose gesture-based game using Python backend and React Native frontend. The game uses MediaPipe for pose detection and tracking.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Backend (Python)](#backend-python)
4. [Frontend (React Native)](#frontend-react-native)
5. [Gameplay](#gameplay)
6. [Features](#features)
7. [Requirements](#requirements)

## Project Overview

Pose Tracking Game is a fun interactive application that uses computer vision to detect and track pose gestures. Users can interact with virtual objects in the game environment using their poses. The project combines real-time video processing with React Native for a seamless mobile gaming experience.

## Setup Instructions

To set up the project, follow these steps:

1. Clone the repository:
git clone from https://github.com/NafisRayan/PoseTrackingGame-DZK 


2. Set up Python virtual environment:
python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate 
pip install flask cv2 mediapipe numpy


3. Install dependencies for React Native:
npm i


4. Start the Flask server:
python app.py


5. Run the React Native app:
npm start


## Backend (Python)

The backend is built using Flask and utilizes OpenCV and MediaPipe for real-time pose tracking.

### Key Features

- Uses MediaPipe poses for accurate pose landmark detection
- Implements a scoring system based on successful circle touches
- Generates random circle positions for continuous gameplay
- Provides a live video stream of the game environment

### Code Structure

The Python backend (`app.py`) consists of:

1. Flask application setup
2. MediaPipe poses initialization
3. Circle generation and management functions
4. Video stream generation
5. Flask routes for serving the game page and video feed

## Frontend (React Native)

The frontend is built using React Native and Expo for mobile app development.

### Key Features

- Responsive UI design for mobile devices
- Real-time video streaming from the backend
- Connection status indicator
- Error poseling for network issues

### Code Structure

The React Native frontend (`App.js`) consists of:

1. Component structure for the main app layout
2. State management for connection status and server URL
3. WebView component for displaying the game environment
4. Error poseling and alert components

## Gameplay

1. The game displays a live video stream of the player's camera view.
2. A circle appears randomly in the frame after a short delay.
3. Players must touch the circle with their index finger tip to score points.
4. The circle disappears and reappears at random positions throughout the game.
5. The current score is displayed on the screen.

## Features

- Real-time pose tracking using MediaPipe poses
- Random circle placement for continuous gameplay
- Score tracking and display
- Mobile-friendly interface with React Native
- Cross-platform support (iOS and Android)

## Requirements

- Python 3.8+
- Node.js 14+
- npm 6+
- Android SDK or iOS simulator
