class Skill:
    def __init__(self, experience_curve, base_perk_points, derivative_perk_points, perk_credits, level=1, experience=0, name='', description='',  involved_stats={}):
        self.level = level
        self.experience = experience
        self.name = name
        self.description = description
        self.involved_stats = involved_stats