from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
	slide_1 = url_for("static", filename="slides/Slide3.jpg")
	slide_2 = url_for("static", filename="slides/slide5.jpg")
	slide_3 = url_for("static", filename="slides/slide1.jpg")
	slide_4 = url_for("static", filename="slides/slide2.jpg")
	slide_5 = url_for("static", filename="slides/slide4.jpg")
	master =  url_for("static", filename="staff_picture/master.jpg")
	logo = url_for("static", filename="logo/green-logo.png")
	School4 = url_for("static", filename="schoolPicture/school4.jpg")



	primary = [
	             {"title"  :     "School fees 2020",
	              "content":   "In 2020 fee structure is change for both primamry and Baby class.all fee should be paid in our system",
	              "image"  :    slide_1
	             },


	              
	             {"title":      "Graduation and Talent day",
	              "content":    "Graduation for our primamry pupip will be 12th Agust 2020. parent should ..",
	              "image"  :    slide_2
	             },



	             {"title":      "Uniform and Sport items",
	              "content":     "Parent our School Uniform is changed now our pupils will wear Suit and Sweater.." ,
	              "image"  :    slide_3   
	             },



	             {"title":      "Results and Parent forums",
	              "content":    "In 2020 Results of our pupils will be sent to parent Email or Phone number...",
	              "image"  :    slide_4
	             }
	           ]
	return render_template('home.html', title='home',slide_1=slide_1,slide_2=slide_2,slide_3=slide_3,School4=School4,
									slide_4=slide_4,slide_5=slide_5,master=master,logo=logo, primary=primary)



@app.route("/Our_school")
def Our_school():
	slide_1 = url_for("static", filename="slides/Slide3.jpg")
	slide_2 = url_for("static", filename="slides/slide5.jpg")
	slide_3 = url_for("static", filename="slides/slide1.jpg")
	slide_4 = url_for("static", filename="slides/slide2.jpg")
	slide_5 = url_for("static", filename="slides/slide4.jpg")
	master =  url_for("static", filename="staff_picture/master.jpg")
	logo = url_for("static", filename="logo/green-logo.png")
	slide_5 = url_for("static", filename="slides/slide4.jpg")


	School1 = url_for("static", filename="schoolPicture/school1.jpg")
	School2 = url_for("static", filename="schoolPicture/school3.jpg")
	School4 = url_for("static", filename="schoolPicture/school4.jpg")
	return render_template("Our_school.html" ,logo=logo,title="Our School",School2=School2,School4=School4,
									 School1=School1, slide_1=slide_1,slide_2=slide_2,slide_3=slide_3,
									slide_4=slide_4,slide_5=slide_5)


@app.route("/Contact")
def Contact():
	slide_1 = url_for("static", filename="slides/Slide3.jpg")
	slide_2 = url_for("static", filename="slides/slide5.jpg")
	slide_3 = url_for("static", filename="slides/slide1.jpg")
	slide_4 = url_for("static", filename="slides/slide2.jpg")
	slide_5 = url_for("static", filename="slides/slide4.jpg")
	master =  url_for("static", filename="staff_picture/master.jpg")
	logo = url_for("static", filename="logo/green-logo.png")
	
	return render_template("Contact.html",logo=logo,title="Contact",slide_1=slide_1,slide_2=slide_2,slide_3=slide_3,
									slide_4=slide_4,slide_5=slide_5)



@app.route("/News")
def News():
	slide_1 = url_for("static", filename="slides/Slide3.jpg")
	slide_2 = url_for("static", filename="slides/slide5.jpg")
	slide_3 = url_for("static", filename="slides/slide1.jpg")
	slide_4 = url_for("static", filename="slides/slide2.jpg")
	slide_5 = url_for("static", filename="slides/slide4.jpg")
	master =  url_for("static", filename="staff_picture/master.jpg")
	logo = url_for("static", filename="logo/green-logo.png")


	primary = [
	             {"title"  :     "School fees 2020",
	              "content":   "In 2020 fee structure is change for both primamry and Baby class.all fee should be paid in our system In 2020 fee structure is change for both primamry and Baby class.all fee should be paid in our systemIn 2020 fee structure is change for both primamry and Baby class.all fee should be paid in our system",
	              "image"  :    slide_1
	             },


	              
	             {"title":      "Graduation and Talent day",
	              "content":    "Graduation for our primamry pupip will be 12th Agust 2020. parent should Graduation for our primamry pupip will be 12th Agust 2020. parent shouldGraduation for our primamry pupip will be 12th Agust 2020. parent should",
	              "image"  :    slide_2
	             },



	             {"title":      "Uniform and Sport items",
	              "content":     "Parent our School Uniform is changed now our pupils will wear Suit and Sweater Parent our School Uniform is changed now our pupils will wear Suit and SweaterParent our School Uniform is changed now our pupils will wear Suit and Sweater" ,
	              "image"  :    slide_3   
	             },



	             {"title":      "Results and Parent forums",
	              "content":    "In 2020 Results of our pupils will be sent to parent Email or Phone number In 2020 Results of our pupils will be sent to parent Email or Phone numberIn 2020 Results of our pupils will be sent to parent Email or Phone number",
	              "image"  :    slide_4
	             }
	           ]
	return render_template("News.html",logo=logo,title="News",slide_1=slide_1,slide_2=slide_2,slide_3=slide_3,
									slide_4=slide_4,slide_5=slide_5,primary=primary)



@app.route("/Learning")
def Learning():
	slide_1 = url_for("static", filename="slides/Slide3.jpg")
	slide_2 = url_for("static", filename="slides/slide5.jpg")
	slide_3 = url_for("static", filename="slides/slide1.jpg")
	slide_4 = url_for("static", filename="slides/slide2.jpg")
	slide_5 = url_for("static", filename="slides/slide4.jpg")
	master =  url_for("static", filename="staff_picture/master.jpg")
	logo = url_for("static", filename="logo/green-logo.png")
	return render_template("Learning.html",logo=logo,title="Learning",slide_1=slide_1,slide_2=slide_2,slide_3=slide_3,
									slide_4=slide_4,slide_5=slide_5)



@app.route("/Key_Information")
def Key_Information():
	slide_1 = url_for("static", filename="slides/Slide3.jpg")
	slide_2 = url_for("static", filename="slides/slide5.jpg")
	slide_3 = url_for("static", filename="slides/slide1.jpg")
	slide_4 = url_for("static", filename="slides/slide2.jpg")
	slide_5 = url_for("static", filename="slides/slide4.jpg")
	master =  url_for("static", filename="staff_picture/master.jpg")
	logo = url_for("static", filename="logo/green-logo.png")

	termdate = url_for("static", filename="schoolPicture/termdate.jpg")
	return render_template("Key_Information.html",logo=logo,title="Key Information",termdate=termdate,slide_1=slide_1,slide_2=slide_2,slide_3=slide_3,
									slide_4=slide_4,slide_5=slide_5)	



if __name__ == '__main__':
	app.run(debug=True)