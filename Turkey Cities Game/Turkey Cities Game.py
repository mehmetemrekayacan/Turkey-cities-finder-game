import turtle
import pandas


cities= {"İller": [
        "adana", "adıyaman", "afyonkarahisar", "ağrı", "amasya", "ankara", "antalya", "artvin", "aydın", 
        "balıkesir", "bilecik", "bingöl", "bitlis", "bolu", "burdur", "bursa", "çanakkale", "çankırı", "çorum",
        "denizli", "diyarbakır", "edirne", "elazığ", "erzincan", "erzurum", "eskişehir", "gaziantep", "giresun",
        "gümüşhane", "hakkari", "hatay", "ısparta", "mersin", "istanbul", "izmir", "kars", "kastamonu", "kayseri",
        "kırklareli", "kırşehir", "kocaeli", "konya", "kütahya", "malatya", "manisa", "kahramanmaraş", "mardin",
        "muğla", "muş", "nevşehir", "niğde", "ordu", "rize", "samsun", "siirt", "sinop", "sivas", "tekirdağ", "tokat",
        "trabzon", "tunceli", "şanlıurfa", "uşak", "van", "yozgat", "zonguldak", "aksaray", "bayburt", "karaman",
        "kırıkkale", "batman", "şırnak", "bartın", "ardahan", "ığdır", "yalova", "karabük", "kilis", "osmaniye",
        "düzce"
    ],
"koordinatlar_x" : [5.0, 144.0, -254.0, 397.0, 19.0, -144.0, -254.0, 329.0, -400.0, -393.0, -276.0, 279.0, 355.0, -191.0, -289.0, -329.0, -461.0, -103.0, -41.0, -336.0, 262.0, -455.0, 198.0, 188.0, 314.0, -231.0, 111.0, 162.0, 207.0, 452.0, 45.0, -240.0, -77.0, -327.0, -453.0, 396.0, -86.0, 18.0, -399.0, -66.0, -248.0, -158.0, -304.0, 138.0, 14.0, 79.0, 288.0, -389.0, 327.0, -38.0, -39.0, 107.0, 279.0, 32.0, 356.0, -23.0, 98.0, -414.0, 61.0, 221.0, 212.0, 194.0, -323.0, 443.0, -10.0, -184.0, -81.0, 249.0, -117.0, -89.0, 314.0, 379.0, -148.0, 383.0, 448.0, -323.0, -142.0, 89.0, 44.0, -213.0],

"koordinatlar_y" : [-133.0, -93.0, -24.0, 42.0, 102.0, 49.0, -142.0, 141.0, -82.0, 50.0, 70.0, -8.0, -43.0, 99.0, -106.0, 76.0, 87.0, 102.0, 87.0, -84.0, -72.0, 170.0, -37.0, 37.0, 65.0, 34.0, -144.0, 103.0, 80.0, -97.0, -193.0, -81.0, -166.0, 143.0, -39.0, 98.0, 153.0, -39.0, 188.0, 7.0, 113.0, -73.0, 18.0, -37.0, 100.0, -94.0, -119.0, -135.0, -11.0, -34.0, -88.0, 112.0, 126.0, 143.0, -76.0, 181.0, 27.0, 143.0, 80.0, 122.0, 4.0, -138.0, -31.0, -32.0, 28.0, 148.0, -56.0, 78.0, -133.0, 45.0, -84.0, -107.0, 171.0, 145.0, 65.0, 108.0, 135.0, -162.0, -131.0, 122.0]
}

data=pandas.DataFrame(cities)
all_cities=data["İller"].to_list()

screen=turtle.Screen()
screen.title("Turkey Cities Game")

image="Turkey Cities Game\Turkey_map_city_limits.gif"
screen.addshape(image)
turtle.shape(image)

correct=0
game=True
while game:
    answer_cities=screen.textinput(title=f"{correct}/81 Guess Correct",prompt="What's another city's name?")
    if answer_cities is None:
        game=False
        screen.bye()
    if answer_cities in all_cities:
        correct+=1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["İller"]==answer_cities]
        x_coord = state_data["koordinatlar_x"].item()
        y_coord = state_data["koordinatlar_y"].item()
        t.goto(x_coord, y_coord)
        t.write(answer_cities)
    

screen.exitonclick()