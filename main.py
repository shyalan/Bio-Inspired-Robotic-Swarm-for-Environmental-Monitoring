from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    # Retrieve values from the form
    num_swarms = int(request.form['num_swarms'])
    temperature_random = request.form.get('temperature', '')
    terrain_size = int(request.form['terrain_size'])
    difficulty_level_random = request.form.get('difficulty_level', '')
    time_of_day = request.form['time_of_day']
    humidity_random = request.form.get('humidity', '')
    air_quality_random = request.form.get('air_quality', '')
    sound_levels_random = request.form.get('sound_levels', '')
    gasses_random = request.form.get('gasses', '')

    # Assign random values if the 'random' checkbox is checked
    temperature = random.randint(-15, 100) if temperature_random == 'on' or temperature_random == '' else int(temperature_random)
    difficulty_level = random.randint(1, 10) if difficulty_level_random == 'on' or difficulty_level_random == '' else int(difficulty_level_random)
    humidity = random.randint(0, 100) if humidity_random == 'on' or humidity_random == '' else int(humidity_random)
    air_quality = random.randint(0, 100) if air_quality_random == 'on' or air_quality_random == '' else int(air_quality_random)
    sound_levels = random.randint(0, 100) if sound_levels_random == 'on' or sound_levels_random == '' else int(sound_levels_random)
    gasses = random.randint(0, 100) if gasses_random == 'on' or gasses_random == '' else int(gasses_random)

    # Store values
    simulation_data = {
        'num_swarms': num_swarms,
        'temperature': temperature,
        'terrain_size': terrain_size,
        'difficulty_level': difficulty_level,
        'time_of_day': time_of_day,
        'humidity': humidity,
        'air_quality': air_quality,
        'sound_levels': sound_levels,
        'gasses': gasses,
    }

    # Pass the values to the simulation page
    return render_template('simulate.html', simulation_data=simulation_data)

if __name__ == '__main__':
    app.run(debug=True)
