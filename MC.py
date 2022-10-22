import random as r
import configparser
import os
import webbrowser
import sys
from tkinter import *


def winquit():
        win.quit
        
def makeconfig():
        #this makes the config file, yo.
        global win
        win = Tk()
        global winff
        global winsd
        global winhc
        global winlc
        global wingf
        if win.state()=='normal':
                win.withdraw()
        config=configparser.ConfigParser()
        con='config.ini'
        with open(con, 'w') as f:
                config.add_section('section_a')
                config.add_section('section_b')
                config.add_section('section_c')
                config.add_section('section_d')
                config.add_section('section_e')
                config.set('section_a', 'a1', 'Mcdonalds')
                config.set('section_a', 'a2', 'Pizza Hut')
                config.set('section_a', 'a3', 'Mcdonalds')
                config.set('section_a', 'a4', 'Burger King')
                config.set('section_a', 'a5', 'Taco Bell')
                config.set('section_a', 'a6', 'Arbys')
                config.set('section_a', 'a7', 'QuikTrip')
                config.set('section_a', 'a8', 'Dairy Queen')
                config.set('section_a', 'a9', 'Freddys')
                config.set('section_a', 'a10', 'Sonic')
                config.set('section_a', 'a11', 'Wendys')
                config.set('section_a', 'a12', 'Chipotle')
                config.set('section_a', 'a13', 'Kentucky Fried Chicken')
                config.set('section_a', 'a14', 'Popeyes')
                config.set('section_a', 'a15', 'Churchs Chicken')
                config.set('section_a', 'a16', 'Jimmy Johns')
                config.set('section_a', 'a17', 'Dunkin Donuts')
                config.set('section_a', 'a18', 'Jack in the Box')
                config.set('section_a', 'a19', 'Dominos Pizza')
                config.set('section_a', 'a20', 'Luftis Fried Fish')
                config.set('section_a', 'a21', 'Big Boy Burgers')
                config.set('section_a', 'a22', 'A&W Restaraunt')
                config.set('section_a', 'a23', 'Hi-Boy Drive-in')
                config.set('section_a', 'a24', 'Five Guys')
                config.set('section_a', 'a25', 'Mugs-Up')
                config.set('section_a', 'a26', 'Pauls Drive-in')
                config.set('section_a', 'a27', 'Long John Silvers')
                config.set('section_a', 'a28', 'Chick-fil-A')
                config.set('section_a', 'a29', 'Hardees')
                config.set('section_a', 'a30', 'Sarpinos Pizza')
                config.set('section_a', 'a0', 'Little Caesars Pizza')
                config.set('section_b', 'b0', 'Las Chilis Mexican')
                config.set('section_b', 'b1', 'Ihop')
                config.set('section_b', 'b3', 'El Magueys')
                config.set('section_b', 'b4', 'Applebees')
                config.set('section_b', 'b5', 'Pepperjax Grill')
                config.set('section_b', 'b6', 'Los Compas Mexican')
                config.set('section_b', 'b7', 'Dennys')
                config.set('section_b', 'b8', 'Waffle House')
                config.set('section_b', 'b9', 'Mediterranean Grill')
                config.set('section_b', 'b10', 'Olive Garden')
                config.set('section_b', 'b11', 'Rosies Cafe')
                config.set('section_b', 'b12', 'Three Pigs Barbeque')
                config.set('section_b', 'b13', 'The Soul Shack KC')
                config.set('section_b', 'b14', 'Firebirds Wood Fired Grill')
                config.set('section_b', 'b15', 'Hawaiian Bros Island Grill')
                config.set('section_b', 'b16', 'Jack Stack BBQ')
                config.set('section_b', 'b17', 'Queen Taco')
                config.set('section_b', 'b18', 'Red Lobster')
                config.set('section_b', 'b19', 'Backyard Burgers')
                config.set('section_b', 'b20', 'Houlihans')
                config.set('section_b', 'b21', 'Perkins')
                config.set('section_b', 'b22', 'Cheddars Scratch Kitchen')
                config.set('section_b', 'b23', 'Old Chicago Pizza')
                config.set('section_b', 'b24', 'Pizza Ranch')
                config.set('section_b', 'b25', 'Gates BBQ')
                config.set('section_b', 'b26', 'JJs')
                config.set('section_b', 'b27', 'In-A-Tub')
                config.set('section_b', 'b28', 'Lakewood Local')
                config.set('section_b', 'b29', 'On The Border Mexican Grill')
                config.set('section_b', 'b30', 'Charlestons')
                config.set('section_b', 'b31', 'A Little BBQ Joint')
                config.set('section_b', 'b32', 'Pie Five Pizza')
                config.set('section_b', 'b33', 'Mama Chinas')
                config.set('section_b', 'b34', 'Black Bear Diner')
                config.set('section_b', 'b35', 'King Wok')
                config.set('section_b', 'b36', 'Red Door Woodfired Grill')
                config.set('section_b', 'b37', 'Salty Iguana')
                config.set('section_b', 'b38', 'Siki Japanese Steak House and Sushi Bar')
                config.set('section_b', 'b39', 'Finger Foodz')
                config.set('section_b', 'b40', 'Jess and Jims Steak House')
                config.set('section_b', 'b41', 'Slim Chickens')
                config.set('section_b', 'b42', 'Brio Italian Grill')
                config.set('section_b', 'b43', 'SPIN! Pizza')
                config.set('section_b', 'b44', 'Fritzs at Crown Center')
                config.set('section_b', 'b45', 'Chilis Bar and Grill')
                config.set('section_b', 'b46', 'The Corner Mexican Food')
                config.set('section_b', 'b47', 'Youngs Chinese')
                config.set('section_b', 'b48', 'Bella Napoli')
                config.set('section_b', 'b49', 'Chuys')
                config.set('section_b', 'b50', 'Mint Sushi')
                config.set('section_b', 'b51', 'Tacos El Gallo')
                config.set('section_b', 'b52', 'Sweet Siam Thai')
                config.set('section_b', 'b53', 'Minskys Pizza')
                config.set('section_b', 'b54', 'Jose Peppers Mexican')
                config.set('section_b', 'b55', 'Taco Republic Corinth Square')
                config.set('section_b', 'b56', 'Summit Grill')
                config.set('section_b', 'b57', 'Blue Moose')
                config.set('section_b', 'b58', 'Godfathers Pizza')
                config.set('section_b', 'b59', 'India Palace')
                config.set('section_b', 'b60', 'NIJI Sushi and Steak')
                config.set('section_b', 'b61', '54th Street Bar and Grill')
                config.set('section_c', 'c0', 'Steak and Mashed Potatoes')
                config.set('section_c', 'c1', 'Macaroni and Cheese with Hotdogs')
                config.set('section_c', 'c2', 'Salisbury Steaks')
                config.set('section_c', 'c3', 'Cook the neighbors cat')
                config.set('section_c', 'c4', 'Go to the store and get a frozen pizza!')
                config.set('section_c', 'c5', 'You deserve to be lazy. Restart this app and pick "eat out" instead!')
                config.set('section_c', 'c6', 'Chicken Alfredo')
                config.set('section_c', 'c7', 'Shrimp Alfredo')
                config.set('section_c', 'c8', 'Chili')
                config.set('section_c', 'c9', 'Chicken Bacon Ranch Casserole')
                config.set('section_c', 'c10', 'Angel Hair Pasta')
                config.set('section_c', 'c11', 'Chicken Parmesan')
                config.set('section_c', 'c12', 'Chicken and Corn Chowder')
                config.set('section_c', 'c13', 'Tamale Pie')
                config.set('section_c', 'c14', 'Cheeseburger Salad')
                config.set('section_c', 'c15', 'Chicken Primavera')
                config.set('section_c', 'c16', 'Shrimp Scampi')
                config.set('section_c', 'c17', 'Grilled Mahi-Mahi')
                config.set('section_c', 'c18', 'Shish Kebabs')
                config.set('section_c', 'c19', 'Stuffed Pepper Soup')
                config.set('section_c', 'c20', 'Chicken Saltimbocca')
                config.set('section_c', 'c21', 'Ginger Meatballs with Sesame Broccoli')
                config.set('section_c', 'c22', 'Stuffed Zucchini')
                config.set('section_c', 'c23', 'Huevos Rancheros')
                config.set('section_c', 'c24', 'Shrimp Pesto Pasta')
                config.set('section_c', 'c25', 'Chicken Marsala')
                config.set('section_c', 'c26', 'Stuffed Cabbage')
                config.set('section_c', 'c27', 'Sloppy Joe Casserole')
                config.set('section_c', 'c28', 'Lentil Soup')
                config.set('section_c', 'c29', 'Sheet Pan Salmon Puttanesca')
                config.set('section_c', 'c30', 'Cheeseburgers')
                config.set('section_c', 'c31', 'Stuffed Acorn Squash')
                config.set('section_c', 'c32', 'Cowboy Casserole')
                config.set('section_c', 'c33', 'Pork Chops')
                config.set('section_c', 'c34', 'Tacos')
                config.set('section_c', 'c35', 'Chicken Tacos')
                config.set('section_c', 'c36', 'Taco Salad')
                config.set('section_c', 'c37', 'Homemade Pizza')
                config.set('section_c', 'c38', 'Instant Pot Ribs with Dr.Pepper BBQ Sauce')
                config.set('section_c', 'c39', 'Salmon Burgers with Sesame-Soy Glaze')
                config.set('section_c', 'c40', 'Skillet Lasagna')
                config.set('section_c', 'c41', 'BBQ Meatball Subs')
                config.set('section_c', 'c42', 'Baked Spinach Ravioli with Pesto Cream Sauce')
                config.set('section_c', 'c43', 'Honey Soy Salmon')
                config.set('section_c', 'c44', 'Veggie Stir-Fry')
                config.set('section_c', 'c45', 'Pork Marsala with Mushrooms')
                config.set('section_c', 'c46', 'Pretzel-Crusted Chicken with Broccoli')
                config.set('section_c', 'c47', 'Lemon-Thyme Sheet-Pan Chicken and Potatoes')
                config.set('section_c', 'c48', 'Steakhouse Mashed Potato Bowls')
                config.set('section_c', 'c49', 'Chicken Tortilla Soup')
                config.set('section_c', 'c50', 'Cocunut Curry Shrimp with Potatoes')
                config.set('section_c', 'c51', 'Beef Taco Skillet')
                config.set('section_c', 'c52', 'Shepards Pie')
                config.set('section_c', 'c53', 'Cashew Chicken')
                config.set('section_c', 'c54', 'Lemon-Garlic Shrimp and Grits')
                config.set('section_c', 'c55', 'Broccoli Cheese Soup')
                config.set('section_c', 'c56', 'Turkey Chili')
                config.set('section_c', 'c57', 'Crispy Chicken Florintine Melt')
                config.set('section_c', 'c58', 'Grilled Chicken and Strawberry Salad Wrap')
                config.set('section_c', 'c59', 'Beef Stroganoff')
                config.set('section_c', 'c60', 'French Dip Sandwiches')
                config.set('section_c', 'c61', 'Chicken Strips with macaroni and cheese')
                config.set('section_c', 'c62', 'Creamy Spinach and Red Pepper Chicken')
                config.set('section_c', 'c63', 'Cold Cuts')
                config.set('section_c', 'c64', 'Spaghetti and Meatballs')
                config.set('section_c', 'c65', 'Catfish with Macaroni on the side')
                config.set('section_c', 'c66', 'Thai inspired Salmon Salad')
                config.set('section_c', 'c67', 'Bacon Wrapped Meatloaf')
                config.set('section_c', 'c68', 'Meatloaf')
                config.set('section_c', 'c69', 'Pumpkin Ravioli')
                config.set('section_c', 'c70', 'Macaroni and Cheese with Bacon and Peas')
                config.set('section_c', 'c71', 'Oven BBQ Chicken')
                config.set('section_c', 'c72', 'Lemon Basil Shrim Risotto')
                config.set('section_c', 'c73', 'Cobb Salad with Homemade Blue Cheese Dressing')
                config.set('section_c', 'c74', 'Peach-Whiskey Barbecue Chicken')
                config.set('section_c', 'c75', 'Baked Spaghetti')
                config.set('section_c', 'c76', 'Parmesan Crusted Tilapia')
                config.set('section_c', 'c77', 'Swedish Meatballs')
                config.set('section_c', 'c78', 'White Chicken Chili')
                config.set('section_c', 'c79', 'Penne with Vodka Sauce and Mini Meatballs')
                config.set('section_c', 'c80', 'Enchiladas')
                config.set('section_c', 'c81', 'Beer Can Chicken')
                config.set('section_c', 'c82', 'Shredded Steak mixed with Instant Mashed potatoes')
                config.set('section_c', 'c83', 'Loaded French Fries')
                config.set('section_c', 'c84', 'Meatloaf with a bed of hashbrowns and eggs on top')
                config.set('section_c', 'c85', 'Pancakes')
                config.set('section_c', 'c86', 'Beef Stew')
                config.set('section_c', 'c87', 'Clam Chowder')
                config.set('section_c', 'c88', 'Bacon and Eggs for Dinner!')
                config.set('section_c', 'c89', 'Oven-baked French Bread Pizzas')
                config.set('section_c', 'c90', 'Easy Butter Chicken')
                config.set('section_c', 'c91', 'Bacon and Egg Ramen Noodles')
                config.set('section_c', 'c92', 'Jumbalaya')
                config.set('section_c', 'c93', 'Garlic Salmon and Asparagus')
                config.set('section_c', 'c94', 'Tuba and Avacado Wrap')
                config.set('section_c', 'c95', 'Teriyaki Chicken and Veggie Foil Packs')
                config.set('section_c', 'c96', 'Stuffed Peppers')
                config.set('section_c', 'c97', '15 Minute Lo Mein')
                config.set('section_c', 'c98', 'Tuna Mornay Rice Bake')
                config.set('section_c', 'c99', 'Chicken and Rice')
                config.set('section_c', 'c100', 'One Tray Haloumi and Chickpea Bake')
                
                config.set('section_d', 'd0', 'Keto Beef Stew')
                config.set('section_d', 'd1', 'Keto Chicken Parmesan')
                config.set('section_d', 'd2', 'Cauliflower Mac and Cheese')
                config.set('section_d', 'd3', 'Avacado Soup')
                config.set('section_d', 'd4', 'Tuscan Butter Shrimp')
                config.set('section_d', 'd5', 'Garlicky Lemon Mahi-Mahi')
                config.set('section_d', 'd6', 'Grilled Tuna Steak with Scallion Sauce')
                config.set('section_d', 'd7', 'Keto Pancakes')
                config.set('section_d', 'd8', 'Bacon-Wrapped Cauliflower')
                config.set('section_d', 'd9', 'Keto Taco Casserole')
                config.set('section_d', 'd10', 'Italian Sausage and Broccoli Rabe Egg Casserole')
                config.set('section_d', 'd11', 'Keto Chili')
                config.set('section_d', 'd12', 'Cheesy Bacon Ranch Chicken')
                config.set('section_d', 'd13', 'Sweet Potato Lasagna')
                config.set('section_d', 'd14', 'Zuccini Apple Crisp')
                config.set('section_d', 'd15', 'Keto Stuffed Cabbage')
                config.set('section_d', 'd16', 'Butternut Squash Noodles')
                config.set('section_d', 'd17', 'Antipasto-Stuffed Chicken')
                config.set('section_d', 'd18', 'Burrito Zucchini Boats')
                config.set('section_d', 'd19', 'Mashed Cauliflower')
                config.set('section_d', 'd20', 'Asian Chicken Lettuce Wraps')
                config.set('section_d', 'd21', 'Eggplant Lasagna')
                config.set('section_d', 'd22', 'Chicken Parm Stuffed Peppers')
                config.set('section_d', 'd23', 'Zucchini Lasagna Roll-ups')
                config.set('section_d', 'd24', 'Egg Roll Bowls')
                config.set('section_d', 'd25', 'Bruschetta Grilled Chicken')
                config.set('section_d', 'd26', 'Ta-Ketos')
                config.set('section_d', 'd27', 'Air')

                config.set('section_e', 'e0', 'Ultimate Chicken Salad')
                config.set('section_e', 'e1', 'Best Baked Salmon')
                config.set('section_e', 'e2', 'Mediterranean Chickpea Salad')
                config.set('section_e', 'e3', 'Zucchini Pasta with Lemon Garlic Shrimp')
                config.set('section_e', 'e4', 'Tuna Salad')
                config.set('section_e', 'e5', 'Baked Chicken Breast')
                config.set('section_e', 'e6', 'Broccoli Salad')
                config.set('section_e', 'e7', 'Egg Salad')
                config.set('section_e', 'e8', 'One Pan Chicken and Rice')
                config.set('section_e', 'e9', 'Falafel')
                config.set('section_e', 'e10', 'Creamy Chipotle Shrimp')
                config.set('section_e', 'e11', 'Stuffed Peppers')
                config.set('section_e', 'e12', 'Chicken Stir-Fry')
                config.set('section_e', 'e13', 'Teriyaki Chicken')
                config.set('section_e', 'e14', 'Cauliflower Pizza Crust')
                config.set('section_e', 'e15', 'Chicken Fajitas')
                config.set('section_e', 'e16', 'Carnitas')
                config.set('section_e', 'e17', 'Paleo Banana Bread')
                config.set('section_e', 'e18', 'Chia Pudding')
                config.set('section_e', 'e19', 'Ice Water')
                config.set('section_e', 'e20', 'Paleo Pancakes')
                config.set('section_e', 'e21', 'Roasted Sweet Potatoes')
                config.set('section_e', 'e22', 'Ice Water (yes, literally just ice water)')
                config.set('section_e', 'e23', 'Loaded Breakfast Casserole')
                
                with open(con, 'w') as configfile:
                    config.write(configfile)
                print(os.getcwd())
                start()

#Define a function to close the window
def close_win():
   win.destroy()
   quit()


def start():
     #this determines where you head next
    if win.state()=='normal':
        win.withdraw()
    win.deiconify()
    #Create a label
    Label(win, text="Paul's Meal Chooser",
    font=('Poppins bold', 25)).pack(pady= 20)
    win.geometry("800x500")
    #Create a Button
    Button(win, text= "Fast Food", font=('Poppins bold', 16),
    command=fastfood).pack(pady=10)
    Button(win, text= "Sit Down Restaurant", font=('Poppins bold', 16),
    command=sitdown).pack(pady=10)
    Button(win, text= "Home Cooked Meal", font=('Poppins bold', 16),
    command=homecook).pack(pady=10)
    Button(win, text= "Random Choice", font=('Poppins bold', 16),
    command=randomizechoice).pack(pady=10)
    Button(win, text= "Low Carb Recipes", font=('Poppins bold', 16),
    command=lowcarb).pack(pady=10)
    Button(win, text= "Gluten Free Recipes", font=('Poppins bold', 16),
    command=glutenfree).pack(pady=10)
    Button(win, text= "Exit Program", font=('Poppins bold', 10),
    command=close_win).pack(pady=5)
    win.mainloop()
    
    

def randomizechoice():
     #this randomizes the choice from start()
    if win.state()=='normal':
        win.withdraw()
    choice=r.randint(0,5)
    if choice==1:
        fastfood()
    elif choice==2:
        sitdown()
    elif choice==3:
        homecook()
    else:
        randomizechoice()

def ffrestart():
    #trying to restart fastfood() if the result didnt sound good.
    winff.destroy()
    fastfood()

def hcrestart():
    #trying to restart homecook() if the result didnt sound good.
    winhc.destroy()
    homecook()

def sdrestart():
    #trying to restart sitdown() if the result didnt sound good.
    winsd.destroy()
    sitdown()

def hcrestart():
    #trying to restart homecook() if the result didnt sound good.
    winhc.destroy()
    homecook()

def lcrestart():
    #trying to restart homecook() if the result didnt sound good.
    winlc.destroy()
    lowcarb()

def gfrestart():
    #trying to restart homecook() if the result didnt sound good.
    wingf.destroy()
    glutenfree()
    
def startrestart():
       #trying to restart start() if its clicked
    start()

def ffstrest():
        winff.destroy()
        start()

def hcstrest():
        winhc.destroy()
        start()

def sdstrest():
        winsd.destroy()
        start()

def lcstrest():
        winlc.destroy()
        start()

def gfstrest():
        wingf.destroy()
        start()

    
def fastfood():
        #this selects a fast food restaurant and outputs the result
    
    global winff
    winff = Tk()
    if win.state()=='normal':
        win.withdraw()
    config = configparser.RawConfigParser()
    config.optionxform = str
    cona = '\config.ini'
    con=(os.getcwd() + cona)
    with open(con, 'r') as f:
        config.read(con)
    rand=r.randint(0,30)
    ff=("a"+str(rand))
    choice = config.get(f'section_a', ff)
    winff.geometry("900x400")
    Label(winff, text=f"Does {choice} sound good?", font=('Poppins bold', 25)).pack(pady= 20)
    Button(winff, text= "Yes", font=('Poppins bold', 16), command=lambda:googleplaceff(choice)).pack(pady=20)
    Button(winff, text= "No", font=('Poppins bold', 16), command=ffrestart).pack(pady=20)
    Button(winff, text= "Start Over", font=('Poppins bold', 16), command=ffstrest).pack(pady=20)
    
        
def googleplaceff(choice):
    if winff.state()=='normal':
        winff.withdraw()
    search= (f'{choice} restaurant')
    webbrowser.open(f'https://www.google.com/search?q={search}')
    global winffl
    winffl = Tk()
    winffl.geometry("700x400")
    Label(winffl, text="Here you go!",
    font=('Poppins bold', 25)).pack(pady= 20)
    Button(winffl, text= "Quit", font=('Poppins bold', 16),
    command=fflquit).pack(pady=20)
    Button(winffl, text= "Start Over", font=('Poppins bold', 16),
    command=closeff).pack(pady=20)

def fflquit():
        winffl.destroy()
        quit()


def googleplacesd(choice):
    if winsd.state()=='normal':
        winsd.withdraw()
    search= (f'{choice} restaurant')
    webbrowser.open(f'https://www.google.com/search?q={search}')
    global winsdl
    winsdl = Tk()
    winsdl.geometry("768x400")
    Label(winsdl, text="I hope you enjoy your night out!",
    font=('Poppins bold', 25)).pack(pady= 20)
    Button(winsdl, text= "Quit", font=('Poppins bold', 16),
    command=sdlquit).pack(pady=20)
    Button(winsdl, text= "Start Over", font=('Poppins bold', 16),
    command=closesd).pack(pady=20)

def sdlquit():
        winsdl.destroy()
        quit()

    
def googlerecipe(choice):
    if winhc.state()=='normal':
        winhc.withdraw()
    search= (f'{choice} recipe')
    webbrowser.open(f'https://www.google.com/search?q={search}')
    global winhcl
    winhcl = Tk()
    winhcl.geometry("700x400")
    Label(winhcl, text="Your Recipe has been searched.",
    font=('Poppins bold', 25)).pack(pady= 20)
    Button(winhcl, text= "Quit", font=('Poppins bold', 16),
    command=hclquit).pack(pady=20)
    Button(winhcl, text= "Start Over", font=('Poppins bold', 16),
    command=closehc).pack(pady=20)

def hclquit():
        winhcl.destroy()
        quit()

def googlerecipelc(choice):
    if winlc.state()=='normal':
        winlc.withdraw()
    search= (f'{choice} recipe')
    webbrowser.open(f'https://www.google.com/search?q={search}+site%3Adelish.com')
    global winlcl
    winlcl = Tk()
    winlcl.geometry("700x400")
    Label(winlcl, text="Your Recipe has been searched.",
    font=('Poppins bold', 25)).pack(pady= 20)
    Button(winlcl, text= "Quit", font=('Poppins bold', 16),
    command=quit).pack(pady=20)
    Button(winlcl, text= "Start Over", font=('Poppins bold', 16),
    command=closelc).pack(pady=20)

def lcquit():
        winlcl.destroy()
        quit()

def googlerecipegf(choice):
    if wingf.state()=='normal':
        wingf.withdraw()
    search= (f'gluten free {choice} recipe')
    webbrowser.open(f'https://www.google.com/search?q={search}+site%3Adownshiftology.com')
    global wingfl
    wingfl = Tk()
    wingfl.geometry("700x400")
    Label(wingfl, text="Please make sure this is Gluten Free.",
    font=('Poppins bold', 25)).pack(pady= 20)
    Button(wingfl, text= "Quit", font=('Poppins bold', 16),
    command=gflquit).pack(pady=20)
    Button(wingfl, text= "Start Over", font=('Poppins bold', 16),
    command=closegf).pack(pady=20)

def gflquit():
        winfgl.destroy()
        quit()

def closehc():
    if winhc.state()=='normal':
        winhc.destroy()
    if winhcl.state()=='normal':
        winhcl.destroy()
        makeconfig()

def closeff():
    if winff.state()=='normal':
        winhc.destroy()
    if winffl.state()=='normal':
        winffl.destroy()
        makeconfig()

def closesd():
    if winsd.state()=='normal':
        winsd.destroy()
    if winsdl.state()=='normal':
        winsdl.destroy()
        makeconfig()

def closelc():
    if winlc.state()=='normal':
        winlc.destroy()
    if winlcl.state()=='normal':
        winlcl.destroy()
        makeconfig()

def closegf():
    if wingf.state()=='normal':
        wingf.destroy()
    if wingfl.state()=='normal':
        wingfl.destroy()
        makeconfig()
    

def sitdown():
    #this selects a 'sit down' restarant, outputs the choice, and then googles it.
    if win.state()=='normal':
        win.withdraw()
    config = configparser.RawConfigParser()
    config.optionxform = str
    cona = '\config.ini'
    con=(os.getcwd() + cona)
    with open(con, 'r') as f:
        config.read(con)
    rand=r.randint(0,61)
    ff=("b"+str(rand))
    choice = config.get(f'section_b', ff)
    global winsd
    winsd= Tk()
    winsd.geometry("700x400")
    Label(winsd, text=f"Does {choice} sound good?", font=('Poppins bold', 25)).pack(pady= 20)
    Button(winsd, text= "Yes", font=('Poppins bold', 16), command=lambda:googleplacesd(choice)).pack(pady=20)
    Button(winsd, text= "No", font=('Poppins bold', 16), command=sdrestart).pack(pady=20)
    Button(winsd, text= "Start Over", font=('Poppins bold', 16), command=sdstrest).pack(pady=20)

def homecook():
    #this selects a meal title and then googles it for you.
    if win.state()=='normal':
        win.withdraw()
    config = configparser.RawConfigParser()
    config.optionxform = str
    cona = '\config.ini'
    con=(os.getcwd() + cona)
    with open(con, 'r') as f:
        config.read(con)
    rand=r.randint(0,100)
    ff=("c"+str(rand))
    choice = config.get(f'section_c', ff)
    global winhc
    winhc= Tk()
    winhc.geometry("700x400")
    Label(winhc, text=f"Does {choice} sound good?", font=('Poppins bold', 25)).pack(pady= 20)
    Button(winhc, text= "Yes", font=('Poppins bold', 16), command=lambda:googlerecipe(choice)).pack(pady=20)
    Button(winhc, text= "No", font=('Poppins bold', 16), command=hcrestart).pack(pady=20)
    Button(winhc, text= "Start Over", font=('Poppins bold', 16), command=hcstrest).pack(pady=20)

def lowcarb():
    #this selects a low carb meal recipe title and then googles it for you.
    if win.state()=='normal':
        win.withdraw()
    config = configparser.RawConfigParser()
    config.optionxform = str
    cona = '\config.ini'
    con=(os.getcwd() + cona)
    with open(con, 'r') as f:
        config.read(con)
    rand=r.randint(0,27)
    ff=("d"+str(rand))
    choice = config.get(f'section_d', ff)
    global winlc
    winlc= Tk()
    winlc.geometry("700x400")
    Label(winlc, text=f"Does {choice} sound good?", font=('Poppins bold', 25)).pack(pady= 20)
    Button(winlc, text= "Yes", font=('Poppins bold', 16), command=lambda:googlerecipelc(choice)).pack(pady=20)
    Button(winlc, text= "No", font=('Poppins bold', 16), command=lcrestart).pack(pady=20)
    Button(winlc, text= "Start Over", font=('Poppins bold', 16), command=lcstrest).pack(pady=20)

def glutenfree():
    #this selects a gluten free meal recipe title and then googles it for you.
    if win.state()=='normal':
        win.withdraw()
    config = configparser.RawConfigParser()
    config.optionxform = str
    cona = '\config.ini'
    con=(os.getcwd() + cona)
    with open(con, 'r') as f:
        config.read(con)
    rand=r.randint(0,23)
    ff=("e"+str(rand))
    choice = config.get(f'section_e', ff)
    global wingf
    wingf= Tk()
    wingf.geometry("700x400")
    Label(wingf, text=f"Does {choice} sound good?", font=('Poppins bold', 25)).pack(pady= 20)
    Button(wingf, text= "Yes", font=('Poppins bold', 16), command=lambda:googlerecipegf(choice)).pack(pady=20)
    Button(wingf, text= "No", font=('Poppins bold', 16), command=gfrestart).pack(pady=20)
    Button(wingf, text= "Start Over", font=('Poppins bold', 16), command=gfstrest).pack(pady=20)

              

makeconfig()

