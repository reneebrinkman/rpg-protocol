class Skill:
    def __init__(self, experience_curve, perk_points, perk_credits, experience=0, name='', description='',  involved_stats={}, stat_values={}):
        self.experience = experience
        self.name = name
        self.description = description
        self.involved_stats = involved_stats
        self.exp_curve = experience_curve
        self.perk_points = perk_points
        self.perk_credits = perk_credits
        self.stat_values = stat_values