import sys
import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import webbrowser

from core.facebookSearchTool import facebookSearchTool

fbtool = facebookSearchTool()

dicFbStalk = {
    "Tags": {
        "Pictures": "https://www.facebook.com/search/%s/photos-of/intersect",
        "Videos": "https://www.facebook.com/search/%s/videos-of/intersect",
        "Publications": "https://www.facebook.com/search/%s/stories-tagged/intersect",
    },
    "Persons": {
        "Family": "https://www.facebook.com/search/%s/relatives/intersect",
        "Friends": "https://www.facebook.com/search/%s/friends/intersect",
        "Common friends": "https://www.facebook.com/search/%s/friends/friends/intersect",
        "Collegues / Employees": "https://www.facebook.com/search/%s/employees/intersect/",
        "School": "https://www.facebook.com/search/%s/schools-attended/ever-past/intersect/students/intersect/",
        "Nearby": "https://www.facebook.com/search/%s/current-cities/residents-near/present/intersect",
    },
    "Visited places": {
        "All": "https://www.facebook.com/search/%s/places-visited/",
        "Bars": "https://www.facebook.com/search/%s/places-visited/110290705711626/places/intersect/",
        "Restaurants": "https://www.facebook.com/search/%s/places-visited/273819889375819/places/intersect/",
        "Shops": "https://www.facebook.com/search/%s/places-visited/200600219953504/places/intersect/",
        "Outside": "https://www.facebook.com/search/%s/places-visited/935165616516865/places/intersect/",
        "Hotels": "https://www.facebook.com/search/%s/places-visited/164243073639257/places/intersect/",
        "Theatres": "https://www.facebook.com/search/%s/places-visited/192511100766680/places/intersect/",
    },
    "Likes": {
        "Pictures": "https://www.facebook.com/search/%s/photos-liked/intersect",
        "Videos": "https://www.facebook.com/search/%s/videos-liked/intersect",
        "Publications": "https://www.facebook.com/search/%s/stories-liked/intersect",
    },
    "Comments": {
        "Pictures": "https://www.facebook.com/search/%s/photos-commented/intersect",
    },
    "Profile": {
        "Pictures": "https://www.facebook.com/search/%s/photos-by/",
        "Videos": "https://www.facebook.com/search/%s/videos-by/",
        "Publications": "https://www.facebook.com/search/%s/stories-by/",
        "Groups": "https://www.facebook.com/search/%s/groups",
        "Future Events": "https://www.facebook.com/search/%s/events-joined/",
        "Past Events": "https://www.facebook.com/search/%s/events-joined/in-past/date/events/intersect/",
        "Games": "https://www.facebook.com/search/%s/apps-used/game/apps/intersect",
        "Apps": "https://www.facebook.com/search/%s/apps-used/",
    },
    "Interests": {
        "Pages": "https://www.facebook.com/search/%s/pages-liked/intersect",
        "Politics": "https://www.facebook.com/search/%s/pages-liked/161431733929266/pages/intersect/",
        "Religion": "https://www.facebook.com/search/%s/pages-liked/religion/pages/intersect/",
        "Musics": "https://www.facebook.com/search/%s/pages-liked/musician/pages/intersect/",
        "Films": "https://www.facebook.com/search/%s/pages-liked/movie/pages/intersect/",
        "Books": "https://www.facebook.com/search/%s/pages-liked/book/pages/intersect/",
        "Places": "https://www.facebook.com/search/%s/places-liked/"
    }
}

resultProfile = """
    [Name]  %s
    [Work]  %s
    [Loc]   %s
    [ID]    %s
    
    """


def search_by_profile(window, search, profile):
    try:
        fbtool.getInfoProfile(profile)

        loc = fbtool.address
        work = fbtool.job
        name = fbtool.name
        facebookID = fbtool.facebookId

        search.destroy()

        old = sys.stdout
        with open("./output.txt", "w", encoding="utf-8") as f:
            sys.stdout = f

            print(resultProfile % (name, work, loc, facebookID))
            search_fb(window, facebookID)
        sys.stdout = old
    except:
        messagebox.showerror("Error!", "An error occured while trying to get this profile !")


def search_by_id(window, search, facebookID):
    search.destroy()

    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f

        print("[ID]\t{}\n".format(facebookID))
        search_fb(window, facebookID)
    sys.stdout = old


def search_fb(window, facebookID):
    search = tk.Toplevel(window)
    search.title("Search facebook")
    search.geometry("400x300")

    tk.Label(search, text="Stalking Facebook ID {}".format(facebookID)).pack(side=tk.TOP, anchor=tk.NW)

    tab_parent = ttk.Notebook(search)
    tab_parent.pack(expand=1, fill="both")

    for name, links in dicFbStalk.items():
        tab = tk.Frame(tab_parent)
        tab_parent.add(tab, text=name)
        for link_name, link in links.items():
            add_button(tab, link_name, link, facebookID)


def add_button(tab, name, link, facebookID):
    tk.Button(tab, text=name, command=lambda: webbrowser.open(link % facebookID)).pack()


def facebook_stalk(window, settings):
    search = tk.Toplevel(window)
    search.title("Facebook")
    search.geometry("400x150")

    city = tk.StringVar()

    frame1 = tk.Frame(search, background="White")
    frame1.pack()
    frame2 = tk.Frame(search, background="White")
    frame2.pack()

    tk.Label(frame1, text="Profile name: ").pack(side=tk.LEFT)
    facebook_name = tk.Entry(frame1)
    facebook_name.pack(side=tk.LEFT)
    tk.Button(frame1, text="Find by profile", command=lambda: search_by_profile(window, search, facebook_name.get())) \
        .pack(side=tk.RIGHT)

    tk.Label(frame2, text="Facebook ID: ").pack(side=tk.LEFT)
    facebook_id = tk.Entry(frame2)
    facebook_id.pack(side=tk.LEFT)
    tk.Button(frame2, text="Find by profile", command=lambda: search_by_id(window, search, facebook_id.get())) \
        .pack(side=tk.RIGHT)

    search.mainloop()


def done(search, code, number):
    search.destroy()
    old = sys.stdout
    with open("./output.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        try:
            x = threading.Thread(target=sp, args=(code, number))
            x.start()
            messagebox.showinfo("Searching", "Currently searching...")
            x.join()
        except:
            messagebox.showinfo("Searching", "Currently searching...")
            sp(code, number)
    sys.stdout = old

    messagebox.showinfo("Result", "The result has been written in the output.txt file")
