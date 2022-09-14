class Club:
    def __init__(self, title, theme, virtual_meetings):
        self._title = title
        self._theme = theme
        self._virtual_meetings = virtual_meetings  # The club has virtual meetings, True or False

    def get_title(self):
        return self._title

    def get_theme(self):
        return self._theme

    def meets_virtually(self):
        return self._virtual_meetings

    def meet_with_other_club(self, another_club):
        """
      Host a joint meeting with another club
      """
        if self.meets_virtually() is True and another_club.meets_virtually() is True:
            print("Club", self.get_title(), "and Club", another_club.get_title(), "can host a joint meeting as they both meet virtually")
        elif another_club.meets_virtually() is not True and self.meets_virtually() is not True:
            print("Club", self.get_title(), "and Club", another_club.get_title(), "can host a joint meeting as they both don't meet virtually")
        else:
            print("Club", self.get_title(), "and Club", another_club.get_title(), "cannot meet together as they both do not have the same meeting style")


#Create Club class objects
club1 = Club("Strength In Numbers", "recreational math", True)
club2 = Club("The Baker Street Irregulars", "mystery fiction", False)
club3 = Club("Food for Thought", "recipe exchange", True)

#see whether they can meet each other
club1.meet_with_other_club(club3)
club2.meet_with_other_club(club1)