from flask import Flask, render_template, request, url_for
from itertools import permutations
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ratings", methods=["GET","POST"])
def ratings():
    if request.method == "GET":
        return render_template("ratings.html")

    # POST request handled below
    hitting = [0.185606061,0.192650171,0.196638655,0.199643494,0.202938432,0.205406094,0.207455429,0.209210877,0.211096045,0.212496285,0.213969898,0.215254237,0.21658134,0.217763031,0.218982804,0.220038219,0.22109314,0.222024867,0.222929136,0.223819838,0.224852071,0.225699936,0.226618705,0.227438995,0.228187919,0.228980322,0.229782228,0.230639731,0.231372549,0.232169954,0.232899023,0.233783077,0.234676007,0.23552216,0.236305657,0.237037037,0.237762238,0.238450075,0.239205765,0.24,0.240702482,0.24137931,0.242040917,0.242717254,0.243396226,0.24407527,0.244858931,0.245588663,0.246305419,0.247005988,0.247689464,0.248515075,0.24911032,0.24964132,0.250405992,0.251208356,0.251879699,0.252727273,0.253384913,0.254045307,0.254775833,0.255639098,0.25644294,0.257053292,0.257751816,0.258565557,0.259380098,0.260175036,0.260869565,0.261815319,0.262631765,0.263565424,0.264534884,0.265426076,0.26619965,0.267288924,0.268326418,0.269366457,0.270436825,0.271501269,0.272440945,0.273556231,0.27457331,0.27581146,0.277227723,0.278699545,0.280188252,0.281785258,0.283255086,0.28468725,0.286603209,0.288524577,0.29091547,0.293644969,0.296559259,0.300656635,0.305280434,0.31116879,0.319981358]
    power = [0.036299585,0.041004251,0.044620755,0.047082751,0.049237248,0.051174876,0.053214564,0.054472397,0.056000113,0.057392915,0.058390992,0.059245961,0.060438811,0.061381289,0.062611807,0.063431627,0.064377715,0.065277405,0.06631378,0.067166458,0.067850468,0.068683288,0.069444444,0.070059679,0.070776038,0.071428571,0.072114954,0.07275588,0.073339821,0.074074074,0.074553499,0.075041064,0.075590551,0.07615457,0.076772976,0.077438325,0.077966102,0.0784939,0.079051383,0.079488627,0.079934773,0.080421049,0.08095952,0.081412636,0.082036692,0.08267165,0.083187896,0.083594119,0.084005054,0.084518274,0.085072495,0.08547566,0.086148649,0.086704129,0.087264154,0.087851901,0.088359258,0.088938125,0.089347079,0.089943864,0.09057971,0.091174962,0.09169875,0.092279878,0.092888244,0.093502377,0.094177084,0.094679274,0.095376523,0.095964543,0.096599418,0.097281831,0.097918371,0.098530915,0.099046098,0.099640002,0.100313334,0.100951364,0.101596517,0.102187336,0.102880031,0.103703704,0.1046875,0.105384185,0.106377913,0.107222024,0.107954545,0.109004739,0.109904508,0.110889128,0.112034072,0.11332008,0.114371174,0.115737658,0.117101388,0.119517392,0.1217637,0.124404326,0.129624698]
    walks = [0.028952836,0.035171386,0.03805871,0.039987552,0.041736891,0.044164785,0.045795426,0.047611284,0.049153828,0.050847458,0.052119227,0.053850573,0.055115264,0.056493207,0.057531122,0.058732612,0.05979729,0.060720602,0.061640024,0.0625,0.06332134,0.064467301,0.065349842,0.066306917,0.067312452,0.06841998,0.069486405,0.070111194,0.070791481,0.071826338,0.072628946,0.073380116,0.074188563,0.074766355,0.075728155,0.076486586,0.077288265,0.07809582,0.078869048,0.079484364,0.080128205,0.080773083,0.081339713,0.082240534,0.083006069,0.084006462,0.084656085,0.085393119,0.086325339,0.087266381,0.08810953,0.088945828,0.089715052,0.090518025,0.091316364,0.092340185,0.093369763,0.094350536,0.095468837,0.096651342,0.097645486,0.098296023,0.099236042,0.100286871,0.101204624,0.102423378,0.10308905,0.103992984,0.104677115,0.105942231,0.107264824,0.108347927,0.109375,0.110783468,0.112514857,0.113597047,0.114657554,0.116000454,0.117557684,0.119039161,0.120426829,0.121994736,0.123385244,0.125177797,0.126789437,0.129032258,0.131035236,0.132782477,0.134675086,0.136527654,0.13966913,0.142857143,0.146059537,0.148947635,0.152985379,0.157242485,0.163271672,0.171702816,0.185675852]
    steals = [0,0,0,0,0,0,0,0,0.006230202,0.006414392,0.006622517,0.006802721,0.006993007,0.007194245,0.007518797,0.008049032,0.012578616,0.012820513,0.013157895,0.013513514,0.013888889,0.014388489,0.014925373,0.016260163,0.018987342,0.019480519,0.020134228,0.020833333,0.02189781,0.022900763,0.025,0.025806452,0.026490066,0.027727969,0.028571429,0.030075188,0.031581282,0.032467532,0.033333333,0.034578544,0.03649635,0.037974684,0.039215686,0.040322581,0.042553191,0.044025157,0.045357771,0.046875,0.048387097,0.050359712,0.051948052,0.053691275,0.055944056,0.057373917,0.059602649,0.061728395,0.063798618,0.065693431,0.068493151,0.070063694,0.072847682,0.075471698,0.078316964,0.081081081,0.083333333,0.085977856,0.088211247,0.091549296,0.094352994,0.097402597,0.1,0.103896104,0.10738255,0.111111111,0.115107914,0.119205298,0.124031008,0.1275996,0.130718954,0.135802469,0.140974875,0.14599563,0.151295334,0.157232704,0.162790698,0.169380813,0.176470588,0.183476793,0.192307692,0.201294617,0.20979021,0.219305037,0.227848101,0.245033113,0.259259259,0.28030303,0.309381638,0.349637842,0.389824666]
    caughtStealing = [0.128538084,0.108945578,0.100106918,0.092467236,0.085513566,0.080745342,0.076923077,0.073825503,0.070468581,0.068027211,0.065217391,0.063829787,0.062015504,0.059701493,0.057692308,0.056603774,0.054421769,0.052631579,0.051282051,0.050314465,0.048780488,0.046979866,0.04580003,0.044810563,0.04379562,0.042857143,0.041666667,0.040322581,0.039473684,0.038961039,0.038216561,0.037545113,0.037037037,0.035714286,0.034722222,0.034013605,0.033333333,0.032679739,0.032258065,0.031746032,0.03125,0.030075188,0.028571429,0.027972028,0.027210884,0.026659587,0.026143791,0.025806452,0.025477707,0.025,0.024,0.022727273,0.022058824,0.021582734,0.021126761,0.020689655,0.020134228,0.019736842,0.019480519,0.01910828,0.018867925,0.01863354,0.016260163,0.015267176,0.014814815,0.014492754,0.014184397,0.013986014,0.013793103,0.013513514,0.013333333,0.013071895,0.012903226,0.012738854,0.0125,0.008264463,0.007751938,0.007462687,0.00729927,0.007142857,0.007042254,0.006896552,0.006802721,0.006711409,0.006578947,0.006493506,0.006410256,0.006289308,0.00617284,0,0,0,0,0,0,0,0,0,0]
    hx = [3.437, 3.571, 3.303, 3.097, 2.833, 2.590, 2.718, 2.466, 2.507]
    wx = [3.088, 2.564, 2.164, 2.631, 2.497, 2.495, 2.012, 2.009, 2.105]
    xbx = [1.038, 1.402, 1.310, 1.348, 1.477, 1.137, 0.889, 1.391, 0.458]
    sbx = [0.202, 0.052, 0.141, 0.235, 0.204, 0.042, 0.326, 0.694, -0.106]
    csx = [-0.558, -0.249, -0.147, -0.064, -0.527, -.907, 0.436, -0.196, 0.382]

    p1Name = request.form.get("p1Name")
    p1Hitting = int(request.form.get("p1Hitting"))
    p1Power = int(request.form.get("p1Power"))
    p1Walks = int(request.form.get("p1Walks"))
    p1Speed = int(request.form.get("p1Speed"))

    p2Name = request.form.get("p2Name")
    p2Hitting = int(request.form.get("p2Hitting"))
    p2Power = int(request.form.get("p2Power"))
    p2Walks = int(request.form.get("p2Walks"))
    p2Speed = int(request.form.get("p2Speed"))

    p3Name = request.form.get("p3Name")
    p3Hitting = int(request.form.get("p3Hitting"))
    p3Power = int(request.form.get("p3Power"))
    p3Walks = int(request.form.get("p3Walks"))
    p3Speed = int(request.form.get("p3Speed"))

    p4Name = request.form.get("p4Name")
    p4Hitting = int(request.form.get("p4Hitting"))
    p4Power = int(request.form.get("p4Power"))
    p4Walks = int(request.form.get("p4Walks"))
    p4Speed = int(request.form.get("p4Speed"))

    p5Name = request.form.get("p5Name")
    p5Hitting = int(request.form.get("p5Hitting"))
    p5Power = int(request.form.get("p5Power"))
    p5Walks = int(request.form.get("p5Walks"))
    p5Speed = int(request.form.get("p5Speed"))

    p6Name = request.form.get("p6Name")
    p6Hitting = int(request.form.get("p6Hitting"))
    p6Power = int(request.form.get("p6Power"))
    p6Walks = int(request.form.get("p6Walks"))
    p6Speed = int(request.form.get("p6Speed"))

    p7Name = request.form.get("p7Name")
    p7Hitting = int(request.form.get("p7Hitting"))
    p7Power = int(request.form.get("p7Power"))
    p7Walks = int(request.form.get("p7Walks"))
    p7Speed = int(request.form.get("p7Speed"))

    p8Name = request.form.get("p8Name")
    p8Hitting = int(request.form.get("p8Hitting"))
    p8Power = int(request.form.get("p8Power"))
    p8Walks = int(request.form.get("p8Walks"))
    p8Speed = int(request.form.get("p8Speed"))

    p9Name = request.form.get("p9Name")
    p9Hitting = int(request.form.get("p9Hitting"))
    p9Power = int(request.form.get("p9Power"))
    p9Walks = int(request.form.get("p9Walks"))
    p9Speed = int(request.form.get("p9Speed"))


    pn = []
    pn.extend((p1Name, p2Name, p3Name, p4Name, p5Name, p6Name, p7Name, p8Name, p9Name))
    # pn.extend(("Sanchez", "Voit", "LeMahieu", "Torres", "Urshela", "Stanton", "Tauchamn", "Judge", "Andujar"))
    ph = []
    ph.extend((hitting[p1Hitting-1], hitting[p2Hitting-1], hitting[p3Hitting-1], hitting[p4Hitting-1], hitting[p5Hitting-1], hitting[p6Hitting-1], hitting[p7Hitting-1], hitting[p8Hitting-1], hitting[p9Hitting-1]))
    # ph.extend((0.206, 0.222, 0.301, 0.252, 0.292, 0.236, 0.243, 0.230, 0.122))
    pw =[]
    pw.extend((walks[p1Walks-1], walks[p2Walks-1], walks[p3Walks-1], walks[p4Walks-1], walks[p5Walks-1], walks[p6Walks-1], walks[p7Walks-1], walks[p8Walks-1], walks[p9Walks-1]))
    # pw.extend((0.090, 0.139, 0.070, 0.079, 0.053, 0.167, 0.115, 0.143, 0.020))
    pxb = []
    pxb.extend((power[p1Power-1], power[p2Power-1], power[p3Power-1], power[p4Power-1], power[p5Power-1], power[p6Power-1], power[p7Power-1], power[p8Power-1], power[p9Power-1]))
    # pxb.extend((0.105, 0.076, 0.093, 0.106, 0.116, 0.083, 0.108, 0.103, 0.000))
    psb = []
    psb.extend((steals[p1Speed-1], steals[p2Speed-1], steals[p3Speed-1], steals[p4Speed-1], steals[p5Speed-1], steals[p6Speed-1], steals[p7Speed-1], steals[p8Speed-1], steals[p9Speed-1]))
    # psb.extend((0, 0, 5, 5, 1, 0, 6, 3, 0))
    pcs = []
    pcs.extend((caughtStealing[p1Speed-1], caughtStealing[p2Speed-1], caughtStealing[p3Speed-1], caughtStealing[p4Speed-1], caughtStealing[p5Speed-1], caughtStealing[p6Speed-1], caughtStealing[p7Speed-1], caughtStealing[p8Speed-1], caughtStealing[p9Speed-1]))
    # pcs.extend((1, 0, 2, 2, 1, 0, 0, 2, 0))


    output = open("newlineups.txt", "w")
    combos = list(permutations(range(9), 9))
    hirpg = 0
    lineupRec = ""
    for p in combos:
        rpg = 0
        lineup = ""
        for i in range(9):
            rpg += (hx[i] * ph[p[i]]) + (wx[i] * pw[p[i]]) + (xbx[i] * pxb[p[i]]) + (sbx[i] * psb[p[i]]) + (csx[i] * pcs[p[i]])
            lineup += pn[p[i]]
            lineup += " "
            modrpg = 1.00*(int(rpg * 16200)/100)
        if modrpg > hirpg:
            hirpg = modrpg
            lineupRec = str(modrpg) + " " + lineup + " \n"
            output.write(str(modrpg) + " " + lineup + " \n")

    print(lineupRec)
    return render_template("results.html")

@app.route("/stats", methods=["GET","POST"])
def stats():
    if request.method == "GET":
        return render_template("stats.html")

    # POST request handled below
    counter = 0
    hx = [3.437, 3.571, 3.303, 3.097, 2.833, 2.590, 2.718, 2.466, 2.507]
    wx = [3.088, 2.564, 2.164, 2.631, 2.497, 2.495, 2.012, 2.009, 2.105]
    xbx = [1.038, 1.402, 1.310, 1.348, 1.477, 1.137, 0.889, 1.391, 0.458]
    sbx = [0.202, 0.052, 0.141, 0.235, 0.204, 0.042, 0.326, 0.694, -0.106]
    csx = [-0.558, -0.249, -0.147, -0.064, -0.527, -.907, 0.436, -0.196, 0.382]

    p1Name = request.form.get("p1Name")
    p1PA = float(request.form.get("p1PA"))
    p1HP = float(request.form.get("p1H")) / p1PA
    p1XBHP = float(request.form.get("p1XBH")) / p1PA
    p1WP = float(request.form.get("p1W")) / p1PA
    p1SB = float(request.form.get("p1SB")) / (p1PA / 4)
    p1CS = float(request.form.get("p1CS")) / (p1PA / 4)

    p2Name = request.form.get("p2Name")
    p2PA = float(request.form.get("p2PA"))
    p2HP = float(request.form.get("p2H")) / p2PA
    p2XBHP = float(request.form.get("p2XBH")) / p2PA
    p2WP = float(request.form.get("p2W")) / p2PA
    p2SB = float(request.form.get("p2SB")) / (p2PA / 4)
    p2CS = float(request.form.get("p2CS")) / (p2PA / 4)

    p3Name = request.form.get("p3Name")
    p3PA = float(request.form.get("p3PA"))
    p3HP = float(request.form.get("p3H")) / p3PA
    p3XBHP = float(request.form.get("p3XBH")) / p3PA
    p3WP = float(request.form.get("p3W")) / p3PA
    p3SB = float(request.form.get("p3SB")) / (p3PA / 4)
    p3CS = float(request.form.get("p3CS")) / (p3PA / 4)

    p4Name = request.form.get("p4Name")
    p4PA = float(request.form.get("p4PA"))
    p4HP = float(request.form.get("p4H")) / p4PA
    p4XBHP = float(request.form.get("p4XBH")) / p4PA
    p4WP = float(request.form.get("p4W")) / p4PA
    p4SB = float(request.form.get("p4SB")) / (p4PA / 4)
    p4CS = float(request.form.get("p4CS")) / (p4PA / 4)

    p5Name = request.form.get("p5Name")
    p5PA = float(request.form.get("p5PA"))
    p5HP = float(request.form.get("p5H")) / p5PA
    p5XBHP = float(request.form.get("p5XBH")) / p5PA
    p5WP = float(request.form.get("p5W")) / p5PA
    p5SB = float(request.form.get("p5SB")) / (p5PA / 4)
    p5CS = float(request.form.get("p5CS")) / (p5PA / 4)

    p6Name = request.form.get("p6Name")
    p6PA = float(request.form.get("p6PA"))
    p6HP = float(request.form.get("p6H")) / p6PA
    p6XBHP = float(request.form.get("p6XBH")) / p6PA
    p6WP = float(request.form.get("p6W")) / p6PA
    p6SB = float(request.form.get("p6SB")) / (p6PA / 4)
    p6CS = float(request.form.get("p6CS")) / (p6PA / 4)

    p7Name = request.form.get("p7Name")
    p7PA = float(request.form.get("p7PA"))
    p7HP = float(request.form.get("p7H")) / p7PA
    p7XBHP = float(request.form.get("p7XBH")) / p7PA
    p7WP = float(request.form.get("p7W")) / p7PA
    p7SB = float(request.form.get("p7SB")) / (p7PA / 4)
    p7CS = float(request.form.get("p7CS")) / (p7PA / 4)

    p8Name = request.form.get("p8Name")
    p8PA = float(request.form.get("p8PA"))
    p8HP = float(request.form.get("p8H")) / p8PA
    p8XBHP = float(request.form.get("p8XBH")) / p8PA
    p8WP = float(request.form.get("p8W")) / p8PA
    p8SB = float(request.form.get("p8SB")) / (p8PA / 4)
    p8CS = float(request.form.get("p8CS")) / (p8PA / 4)

    p9Name = request.form.get("p9Name")
    p9PA = float(request.form.get("p9PA"))
    p9HP = float(request.form.get("p9H")) / p9PA
    p9XBHP = float(request.form.get("p9XBH")) / p9PA
    p9WP = float(request.form.get("p9W")) / p9PA
    p9SB = float(request.form.get("p9SB")) / (p9PA / 4)
    p9CS = float(request.form.get("p9CS")) / (p9PA / 4)


    pn = []
    pn.extend((p1Name, p2Name, p3Name, p4Name, p5Name, p6Name, p7Name, p8Name, p9Name))
    # pn.extend(("Sanchez", "Voit", "LeMahieu", "Torres", "Urshela", "Stanton", "Tauchamn", "Judge", "Andujar"))
    ph = []
    ph.extend((p1HP, p2HP, p3HP, p4HP, p5HP, p6HP, p7HP, p8HP, p9HP))
    # ph.extend((0.206, 0.222, 0.301, 0.252, 0.292, 0.236, 0.243, 0.230, 0.122))
    pw =[]
    pw.extend((p1WP, p2WP, p3WP, p4WP, p5WP, p6WP, p7WP, p8WP, p9WP))
    # pw.extend((0.090, 0.139, 0.070, 0.079, 0.053, 0.167, 0.115, 0.143, 0.020))
    pxb = []
    pxb.extend((p1XBHP, p2XBHP, p3XBHP, p4XBHP, p5XBHP, p6XBHP, p7XBHP, p8XBHP, p9XBHP))
    # pxb.extend((0.105, 0.076, 0.093, 0.106, 0.116, 0.083, 0.108, 0.103, 0.000))
    psb = []
    psb.extend((p1SB, p2SB, p3SB, p4SB, p5SB, p6SB, p7SB, p8SB, p9SB))
    # psb.extend((0, 0, 5, 5, 1, 0, 6, 3, 0))
    pcs = []
    pcs.extend((p1CS, p2CS, p3CS, p4CS, p5CS, p6CS, p7CS, p8CS, p9CS))
    # pcs.extend((1, 0, 2, 2, 1, 0, 0, 2, 0))


    output = open("newlineups.txt", "w")
    combos = list(permutations(range(9), 9))
    hirpg = 0
    lineupRec = ""
    for p in combos:
        rpg = 0
        lineup = ""
        for i in range(9):
            rpg += (hx[i] * ph[p[i]]) + (wx[i] * pw[p[i]]) + (xbx[i] * pxb[p[i]]) + (sbx[i] * psb[p[i]]) + (csx[i] * pcs[p[i]])
            lineup += pn[p[i]]
            lineup += " "
            modrpg = 1.00*(int(rpg * 16200)/100)
        if modrpg > hirpg:
            hirpg = modrpg
            lineupRec = str(modrpg) + " " + lineup + " \n"
            output.write(str(modrpg) + " " + lineup + " \n")

    print(lineupRec)
    return render_template("results.html")



