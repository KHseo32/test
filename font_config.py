# font_config.py
import platform
import matplotlib.pyplot as plt

def configure_font():
    if platform.system() == 'Darwin':
        plt.rc('font', family='AppleGothic')
    else:
        plt.rc('font', family='Malgun Gothic')

# Optional: Call the function to configure font when this module is imported
configure_font()
