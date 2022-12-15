class Topic:
    topics = [] # store all topic objects
    topics_name = [] # store all tname
    def __init__(self, tname, user):
        self.tname = tname
        self._tag=""
        if tname not in self.topics_name:
            self.topics.append(self)
            self.topics_name.append(tname)
    @property
    def tag(self):
        return self._tag
    @tag.setter
    def tag(self, tag):
        self._tag = tag
        
    def related(self):
        related = []
        if self.tag:
            for i in self.topics:
                if i.tag == self.tag and i.tname != self.tname:
                    related.append(i.tname)
            if len(related) == 0:
                return "Currently no related topics."
            else: return related
        else:
            return "This topic haven't been taged."

