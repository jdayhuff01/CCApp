from django.db import models

# Create your models here.







class GameRosters(models.Model):
    team_1_name =  models.CharField(max_length=200)
    p1_team1 = models.CharField(max_length=200)
    p2_team1 = models.CharField(max_length=200)
    p3_team1 = models.CharField(max_length=200)
    p4_team1 = models.CharField(max_length=200)
    p5_team1 = models.CharField(max_length=200)
    p6_team1 = models.CharField(max_length=200)

    team_2_name =  models.CharField(max_length=200)
    p1_team2 = models.CharField(max_length=200)
    p2_team2 = models.CharField(max_length=200)
    p3_team2 = models.CharField(max_length=200)
    p4_team2 = models.CharField(max_length=200)
    p5_team2 = models.CharField(max_length=200)
    p6_team2 = models.CharField(max_length=200)

    #stats
    p11_makes = models.IntegerField(default=0)
    p11_misses = models.IntegerField(default=0)
    p21_makes = models.IntegerField(default=0)
    p21_misses = models.IntegerField(default=0)
    p31_makes = models.IntegerField(default=0)
    p31_misses = models.IntegerField(default=0)
    p41_makes = models.IntegerField(default=0)
    p41_misses = models.IntegerField(default=0)
    p51_makes = models.IntegerField(default=0)
    p51_misses = models.IntegerField(default=0)
    p61_makes = models.IntegerField(default=0)
    p61_misses = models.IntegerField(default=0)
    
    p12_makes = models.IntegerField(default=0)
    p12_misses = models.IntegerField(default=0)
    p22_makes = models.IntegerField(default=0)
    p22_misses = models.IntegerField(default=0)
    p32_makes = models.IntegerField(default=0)
    p32_misses = models.IntegerField(default=0)
    p42_makes = models.IntegerField(default=0)
    p42_misses = models.IntegerField(default=0)
    p52_makes = models.IntegerField(default=0)
    p52_misses = models.IntegerField(default=0)
    p62_makes = models.IntegerField(default=0)
    p62_misses = models.IntegerField(default=0)

    team1_cups = models.IntegerField(default=100)
    team2_cups = models.IntegerField(default=100)

    
    @property
    def shootingPercentageP11(self):
        makes = self.p11_makes
        misses = self.p11_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage

    @property
    def shootingPercentageP21(self):
        makes = self.p21_makes
        misses = self.p21_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage

    @property
    def shootingPercentageP31(self):
        makes = self.p31_makes
        misses = self.p31_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    
    @property
    def shootingPercentageP41(self):
        makes = self.p41_makes
        misses = self.p41_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    
    @property
    def shootingPercentageP51(self):
        makes = self.p51_makes
        misses = self.p51_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    
    @property
    def shootingPercentageP61(self):
        makes = self.p61_makes
        misses = self.p61_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage


    @property
    def shootingPercentageP12(self):
        makes = self.p12_makes
        misses = self.p12_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage

    @property
    def shootingPercentageP22(self):
        makes = self.p22_makes
        misses = self.p22_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage

    @property
    def shootingPercentageP32(self):
        makes = self.p32_makes
        misses = self.p32_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    
    @property
    def shootingPercentageP42(self):
        makes = self.p42_makes
        misses = self.p42_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    
    @property
    def shootingPercentageP52(self):
        makes = self.p52_makes
        misses = self.p52_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    
    @property
    def shootingPercentageP62(self):
        makes = self.p62_makes
        misses = self.p62_misses
        if makes + misses == 0:
            return 0
        percentage = round((makes/(makes+misses))*100, 1)
        return percentage
    



    



