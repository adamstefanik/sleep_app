![Alt text](assets/ui-screenshot.png)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![Tkinter](https://img.shields.io/badge/Tkinter-8.6+-green.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)
                                                                                                                                  
  # NightNest                                                                                                                     
                                                                                                                                  
  A modern desktop app for sleep tracking and analysis. Monitor your sleep quality, heart rate variability, and get personalized  
  tips — all in a clean, intuitive interface.              
                                                                                                                                  
  ## Features                                                                                                                     
                                                           
  **Tracking**                                                                                                                    
  - Sleep Analysis – Key sleep quality metrics at a glance
  - Sleep Index – Quality rating on a scale from 1 to 100  
  - Sleep Details – Bedtime, duration, and number of sleep cycles                                                                 
  - Health Metrics – Resting heart rate and HRV
                                                                                                                                  
  **Interface**                                     
  - Expert Advice – Personalized tips based on your sleep quality
  - Motivational Quotes – Random quotes displayed during data loading                                                             
  - Modern UI – Intuitive design inspired by Ultrahuman
                                                                                                                                  
  ## How to Run                                                                                                                   
                                                           
  1. Clone the repository                                                                                                         
  2. Install dependencies                           
  3. Run the app                                           
                                      
  ```bash
  git clone https://github.com/adamstefanik/sleep_app.git
  cd sleep_app
  pip install -r requirements.txt                                                                                                 
  python main.py
  ```
                                                                                                                
  ## Structure                                         
  ```                                                         
  sleep_app/                          
  ├── __pycache__/
  │   ├── data_generator.cpython-313.pyc
  │   └── gui.cpython-313.pyc
  ├── assets/                                                                                                                     
  │   └── ui-screenshot.png
  ├── bg/                                                                                                                         
  │   ├── bg_fetch_data.jpg                         
  │   ├── bg.jpg                                           
  │   ├── btn.jpg                     
  │   ├── green.jpg
  │   ├── red.jpg                                                                                                                 
  │   └── yellow.jpg
  ├── .gitignore                                                                                                                  
  ├── data_generator.py  # Test data generator      
  ├── gui.py             # Graphical interface             
  ├── LICENSE                         
  ├── main.py            # Main entry point
  ├── quotes.json        # Motivational quotes database                                                                           
  ├── README.md
  └── requirements.txt
  ```                                                 
  ## Tech Stack                                               
                                      
  - Python 3.8+
  - Tkinter
  - Standard library (json, random, time, datetime)
                                                                                                                                  
  ## Requirements
                                                                                                                                  
  - Python 3.8+                                     
                                                           
  ## License                             

  This project was developed as part of my studies in software engineering during my junior year at Univerzita Tomáše Bati v Zlíne
   and is intended for educational purposes. MIT — see LICENSE for details.
