# Sound Therapy AI

## Overview

Sound Therapy AI is a web application designed to provide users with personalized sound therapy sessions. The application utilizes AI to recommend soundscapes and tones based on user preferences and conditions, promoting relaxation and well-being.

## Project Structure

The project consists of the following files and directories:

- `app.py`: Main entry point of the application, responsible for initializing the web server and handling routes.
- `sound_generator.py`: Contains functions for generating various sound therapy audio.
- `ai_recommender.py`: Provides AI-based recommendations for sound therapy sessions.
- `templates/`: Directory containing HTML templates for the application.
  - `index.html`: Main landing page of the application.
  - `player.html`: Audio player interface for controlling sound therapy sessions.
- `static/`: Directory for static files such as CSS and JavaScript.
  - `styles.css`: Styles for the application.
  - `scripts.js`: Client-side JavaScript functionality.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `Dockerfile`: Instructions for building a Docker image for the application.
- `.devcontainer/`: Configuration for the development container.
  - `devcontainer.json`: Settings for the development environment.
- `README.md`: Documentation for the project.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd sound-therapy-ai
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

## Usage

- Visit the landing page to explore sound therapy options.
- Use the audio player to listen to recommended soundscapes and tones.
- Customize your experience based on personal preferences.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
