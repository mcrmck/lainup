from flask import Flask, render_template, request, url_for
from itertools import permutations

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

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
    p1SB = float(request.form.get("p1SB"))
    p1CS = float(request.form.get("p1CS"))

    p2Name = request.form.get("p2Name")
    p2PA = float(request.form.get("p2PA"))
    p2HP = float(request.form.get("p2H")) / p2PA
    p2XBHP = float(request.form.get("p2XBH")) / p2PA
    p2WP = float(request.form.get("p2W")) / p2PA
    p2SB = float(request.form.get("p2SB"))
    p2CS = float(request.form.get("p2CS"))

    p3Name = request.form.get("p3Name")
    p3PA = float(request.form.get("p3PA"))
    p3HP = float(request.form.get("p3H")) / p3PA
    p3XBHP = float(request.form.get("p3XBH")) / p3PA
    p3WP = float(request.form.get("p3W")) / p3PA
    p3SB = float(request.form.get("p3SB"))
    p3CS = float(request.form.get("p3CS"))

    p4Name = request.form.get("p4Name")
    p4PA = float(request.form.get("p4PA"))
    p4HP = float(request.form.get("p4H")) / p4PA
    p4XBHP = float(request.form.get("p4XBH")) / p4PA
    p4WP = float(request.form.get("p4W")) / p4PA
    p4SB = float(request.form.get("p4SB"))
    p4CS = float(request.form.get("p4CS"))

    p5Name = request.form.get("p5Name")
    p5PA = float(request.form.get("p5PA"))
    p5HP = float(request.form.get("p5H")) / p5PA
    p5XBHP = float(request.form.get("p5XBH")) / p5PA
    p5WP = float(request.form.get("p5W")) / p5PA
    p5SB = float(request.form.get("p5SB"))
    p5CS = float(request.form.get("p5CS"))

    p6Name = request.form.get("p6Name")
    p6PA = float(request.form.get("p6PA"))
    p6HP = float(request.form.get("p6H")) / p6PA
    p6XBHP = float(request.form.get("p6XBH")) / p6PA
    p6WP = float(request.form.get("p6W")) / p6PA
    p6SB = float(request.form.get("p6SB"))
    p6CS = float(request.form.get("p6CS"))

    p7Name = request.form.get("p7Name")
    p7PA = float(request.form.get("p7PA"))
    p7HP = float(request.form.get("p7H")) / p7PA
    p7XBHP = float(request.form.get("p7XBH")) / p7PA
    p7WP = float(request.form.get("p7W")) / p7PA
    p7SB = float(request.form.get("p7SB"))
    p7CS = float(request.form.get("p7CS"))

    p8Name = request.form.get("p8Name")
    p8PA = float(request.form.get("p8PA"))
    p8HP = float(request.form.get("p8H")) / p8PA
    p8XBHP = float(request.form.get("p8XBH")) / p8PA
    p8WP = float(request.form.get("p8W")) / p8PA
    p8SB = float(request.form.get("p8SB"))
    p8CS = float(request.form.get("p8CS"))

    p9Name = request.form.get("p9Name")
    p9PA = float(request.form.get("p9PA"))
    p9HP = float(request.form.get("p9H")) / p9PA
    p9XBHP = float(request.form.get("p9XBH")) / p9PA
    p9WP = float(request.form.get("p9W")) / p9PA
    p9SB = float(request.form.get("p9SB"))
    p9CS = float(request.form.get("p9CS"))


    pn = []
    pn.extend((p1Name, p2Name, p3Name, p4Name, p5Name, p6Name, p7Name, p8Name, p9Name))
    ph = []
    ph.extend((p1HP, p2HP, p3HP, p4HP, p5HP, p6HP, p7HP, p8HP, p9HP))
    pw =[]
    pw.extend((p1WP, p2WP, p3WP, p4WP, p5WP, p6WP, p7WP, p8WP, p9WP))
    pxb = []
    pxb.extend((p1XBHP, p2XBHP, p3XBHP, p4XBHP, p5XBHP, p6XBHP, p7XBHP, p8XBHP, p9XBHP))
    psb = []
    psb.extend((p1SB, p2SB, p3SB, p4SB, p5SB, p6SB, p7SB, p8SB, p9SB))
    pcs = []
    pcs.extend((p1CS, p2CS, p3CS, p4CS, p5CS, p6CS, p7CS, p8CS, p9CS))

    slots = 9
    array = range(1, slots)
    lineups = []
    for p in list(permutations(pn)):
        rpg = 0
        lineup = ""
        for i in range(9):
            rpg += (hx[i] * ph[i]) + (wx[i] * pw[i]) + (xbx[i] * pxb[i]) + (sbx[i] * psb[i]) + (csx[i] * pcs[i])
            lineup += pn[i]
            lineup += " "
            modrpg = 1.00*(int(rpg * 16200)/100)
            lineups.append((str(modrpg) + lineup + " \n"))

    lineups.sort()
    print(lineups[0])
    print(ph[0])
    print("hello")
    if request.form.get("language") == "c" or request.form.get("language") == "java" or request.form.get("language") == "python" or request.form.get("language") == "sql" or request.form.get("language") == "html" or request.form.get("language") == "php" or  request.form.get("language") == "javascript":
        counter += 1

    name = request.form.get("name")

    if counter == 7:
        return render_template("zuck.html")

    if counter > 2 and request.form.get("fav_programmer") == "David Malan":
        return render_template("malan.html")

    if request.form.get("hobby") == "philanthropy":
        return render_template("gates.html")
        #return Gates

    if (request.form.get("fav_programmer") == "Zamyla Chen" or request.form.get("fav_programmer") == "David Malan") and (request.form.get("hobby") == "potato" or counter > 2):
        return render_template("rob.html")
        #return Rob

    if request.form.get("application") == "robotics":
        if request.form.get("fav_programmer") == "Clevor Trevor":
            return render_template("will.html")
            #return Will

        if request.form.get("end") == "front_end": #or counter < 3:
            return render_template("jason.html")
            #return jason

        if request.form.get("language") == "javascript":
            return render_template("nathan.html")
            #return Nathan

        return render_template("will.html")

    if request.form.get("application") == "games":
        if counter < 3:
            return render_template("jason.html")
        if request.form.get("fav_programmer") == "Zamyla Chan":
            return render_template("zamyla.html")
            #return Zamyla
        if request.form.get("hobby") == "none":
            return render_template("nathan.html")
            #return Nathan
        if request.form.get("fav_programmer") == "Mark Zuckerberg":
            return render_template("zuck.html")
            #return Zuck

    if request.form.get("application") == "social":
        if counter < 3:
            return render_template("jason.html")
            #return jason

        #return zuck
    if request.form.get("application") == "art":
        return render_template("gries.html")
        #return Gries

    return render_template("will.html")

