from flask import Flask, render_template ,request
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=["POST", "GET"])
def main():
    lis_s = request.form.getlist('subject[]')
    lis_t = request.form.getlist('cal[]')
    if request.method == "POST":
        plt.clf()
        try:
            lis_t = [int(cal) for cal in lis_t if cal.isdigit() and 0 <= int(cal) <= 50]
        except ValueError:
            return "กรุณากรอกคะแนนเป็นตัวเลขในช่วง 0-50", 400
        list_name = []
        lis_t_f = []
        colors = []
        for i, score in enumerate(lis_t):
            if score < 25:
                list_name.append(lis_s[i])
                lis_t_f.append(score)
                colors.append('darkred')
            elif 25 <= score <= 35:
                list_name.append(lis_s[i])
                lis_t_f.append(score)
                colors.append('darkorange')
            else:
                colors.append('limegreen')
        plt.clf()
        plt.xlabel("Subject")
        plt.ylabel("Total")
        plt.ylim(0, 50)
        plt.bar(lis_s, lis_t, color=colors)
        os.makedirs('static', exist_ok=True)
        plt.savefig('static/new_plot.png')
        return render_template('main.html', plot_url='static/new_plot.png', list_name = list_name)
    return render_template('main.html',plot_url=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


