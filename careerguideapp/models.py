# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Acseeyear2016(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30)  # Field name made lowercase.
    studentno = models.CharField(db_column='StudentNo', max_length=20)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=5, blank=True, null=True)  # Field name made lowercase.
    accountancy = models.CharField(db_column='Accountancy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=5, blank=True, null=True)  # Field name made lowercase.
    english = models.CharField(db_column='English', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kiswahili = models.CharField(db_column='Kiswahili', max_length=5, blank=True, null=True)  # Field name made lowercase.
    geography = models.CharField(db_column='Geography', max_length=5, blank=True, null=True)  # Field name made lowercase.
    additionalmathematics = models.CharField(db_column='AdditionalMathematics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    biology = models.CharField(db_column='Biology', max_length=5, blank=True, null=True)  # Field name made lowercase.
    physics = models.CharField(db_column='Physics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.CharField(db_column='Chemistry', max_length=5, blank=True, null=True)  # Field name made lowercase.
    commerce = models.CharField(db_column='Commerce', max_length=5, blank=True, null=True)  # Field name made lowercase.
    agriculture = models.CharField(db_column='Agriculture', max_length=5, blank=True, null=True)  # Field name made lowercase.
    arabiclanguage = models.CharField(db_column='ArabicLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    foodnutrition = models.CharField(db_column='FoodNutrition', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frenchlanguage = models.CharField(db_column='FrenchLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    computerstudies = models.CharField(db_column='ComputerStudies', max_length=5, blank=True, null=True)  # Field name made lowercase.
    economics = models.CharField(db_column='Economics', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acseeYear2016'


class Acseeyear2016Subjectperformance(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=7, blank=True, null=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectgpa = models.CharField(db_column='SubjectGPA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    subjectregranking = models.CharField(db_column='SubjectRegRanking', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectnatranking = models.CharField(db_column='SubjectNatRanking', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acseeYear2016SubjectPerformance'


class Acseeyear2017(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30)  # Field name made lowercase.
    studentno = models.CharField(db_column='StudentNo', max_length=20)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=5, blank=True, null=True)  # Field name made lowercase.
    accountancy = models.CharField(db_column='Accountancy', max_length=5, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=5, blank=True, null=True)  # Field name made lowercase.
    english = models.CharField(db_column='English', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kiswahili = models.CharField(db_column='Kiswahili', max_length=5, blank=True, null=True)  # Field name made lowercase.
    geography = models.CharField(db_column='Geography', max_length=5, blank=True, null=True)  # Field name made lowercase.
    additionalmathematics = models.CharField(db_column='AdditionalMathematics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    biology = models.CharField(db_column='Biology', max_length=5, blank=True, null=True)  # Field name made lowercase.
    physics = models.CharField(db_column='Physics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.CharField(db_column='Chemistry', max_length=5, blank=True, null=True)  # Field name made lowercase.
    commerce = models.CharField(db_column='Commerce', max_length=5, blank=True, null=True)  # Field name made lowercase.
    agriculture = models.CharField(db_column='Agriculture', max_length=5, blank=True, null=True)  # Field name made lowercase.
    arabiclanguage = models.CharField(db_column='ArabicLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    foodnutrition = models.CharField(db_column='FoodNutrition', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frenchlanguage = models.CharField(db_column='FrenchLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    computerstudies = models.CharField(db_column='ComputerStudies', max_length=5, blank=True, null=True)  # Field name made lowercase.
    economics = models.CharField(db_column='Economics', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acseeYear2017'


class Acseeyear2017Subjectperformance(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=7, blank=True, null=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectgpa = models.CharField(db_column='SubjectGPA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    subjectregranking = models.CharField(db_column='SubjectRegRanking', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectnatranking = models.CharField(db_column='SubjectNatRanking', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'acseeYear2017SubjectPerformance'


class Cseeyear2015(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30)  # Field name made lowercase.
    studentno = models.CharField(db_column='StudentNo', max_length=20)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=5, blank=True, null=True)  # Field name made lowercase.
    civics = models.CharField(db_column='Civics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=5, blank=True, null=True)  # Field name made lowercase.
    english = models.CharField(db_column='English', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kiswahili = models.CharField(db_column='Kiswahili', max_length=5, blank=True, null=True)  # Field name made lowercase.
    geography = models.CharField(db_column='Geography', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bibleknowledge = models.CharField(db_column='BibleKnowledge', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basicmathematics = models.CharField(db_column='BasicMathematics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    additionalmathematics = models.CharField(db_column='AdditionalMathematics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    biology = models.CharField(db_column='Biology', max_length=5, blank=True, null=True)  # Field name made lowercase.
    physics = models.CharField(db_column='Physics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.CharField(db_column='Chemistry', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bookkeeping = models.CharField(db_column='BookKeeping', max_length=5, blank=True, null=True)  # Field name made lowercase.
    commerce = models.CharField(db_column='Commerce', max_length=5, blank=True, null=True)  # Field name made lowercase.
    agriculturalsci = models.CharField(db_column='AgriculturalSci', max_length=5, blank=True, null=True)  # Field name made lowercase.
    electricaldraugting = models.CharField(db_column='ElectricalDraugting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    electricalinstallation = models.CharField(db_column='ElectricalInstallation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    electricalengnsci = models.CharField(db_column='ElectricalEngnSci', max_length=5, blank=True, null=True)  # Field name made lowercase.
    elimuyadinikiislam = models.CharField(db_column='ElimuYaDiniKiislam', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fineart = models.CharField(db_column='FineArt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    arabiclanguage = models.CharField(db_column='ArabicLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    archtecturualdraught = models.CharField(db_column='ArchtecturualDraught', max_length=5, blank=True, null=True)  # Field name made lowercase.
    brickworkmasonary = models.CharField(db_column='BrickworkMasonary', max_length=5, blank=True, null=True)  # Field name made lowercase.
    buildingconstruction = models.CharField(db_column='BuildingConstruction', max_length=5, blank=True, null=True)  # Field name made lowercase.
    carpentryjoinery = models.CharField(db_column='CarpentryJoinery', max_length=5, blank=True, null=True)  # Field name made lowercase.
    engineeringsci = models.CharField(db_column='EngineeringSci', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fittingturning = models.CharField(db_column='FittingTurning', max_length=5, blank=True, null=True)  # Field name made lowercase.
    foodnutrition = models.CharField(db_column='FoodNutrition', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frenchlanguage = models.CharField(db_column='FrenchLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    computerstudies = models.CharField(db_column='ComputerStudies', max_length=5, blank=True, null=True)  # Field name made lowercase.
    plumbing = models.CharField(db_column='Plumbing', max_length=5, blank=True, null=True)  # Field name made lowercase.
    music = models.CharField(db_column='Music', max_length=5, blank=True, null=True)  # Field name made lowercase.
    literatureenglish = models.CharField(db_column='LiteratureEnglish', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mechanicaldraughting = models.CharField(db_column='MechanicalDraughting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    motorvehiclemech = models.CharField(db_column='MotorVehicleMech', max_length=5, blank=True, null=True)  # Field name made lowercase.
    paintingsignwriting = models.CharField(db_column='PaintingSignWriting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    physicaleducation = models.CharField(db_column='PhysicalEducation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    radiotvserving = models.CharField(db_column='RadioTvServing', max_length=5, blank=True, null=True)  # Field name made lowercase.
    surveying = models.CharField(db_column='Surveying', max_length=5, blank=True, null=True)  # Field name made lowercase.
    textiledressmaking = models.CharField(db_column='TextileDressMaking', max_length=5, blank=True, null=True)  # Field name made lowercase.
    theatreart = models.CharField(db_column='TheatreArt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    weldingmetalfabrication = models.CharField(db_column='WeldingMetalFabrication', max_length=5, blank=True, null=True)  # Field name made lowercase.
    workshoptech = models.CharField(db_column='WorkshopTech', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cseeYear2015'


class Cseeyear2015Subjectperformance(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=7, blank=True, null=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectgpa = models.CharField(db_column='SubjectGPA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    subjectregranking = models.CharField(db_column='SubjectRegRanking', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectnatranking = models.CharField(db_column='SubjectNatRanking', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cseeYear2015SubjectPerformance'


class Cseeyear2016(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30)  # Field name made lowercase.
    studentno = models.CharField(db_column='StudentNo', max_length=20)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=5, blank=True, null=True)  # Field name made lowercase.
    civics = models.CharField(db_column='Civics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=5, blank=True, null=True)  # Field name made lowercase.
    english = models.CharField(db_column='English', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kiswahili = models.CharField(db_column='Kiswahili', max_length=5, blank=True, null=True)  # Field name made lowercase.
    geography = models.CharField(db_column='Geography', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bibleknowledge = models.CharField(db_column='BibleKnowledge', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basicmathematics = models.CharField(db_column='BasicMathematics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    additionalmathematics = models.CharField(db_column='AdditionalMathematics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    biology = models.CharField(db_column='Biology', max_length=5, blank=True, null=True)  # Field name made lowercase.
    physics = models.CharField(db_column='Physics', max_length=5, blank=True, null=True)  # Field name made lowercase.
    chemistry = models.CharField(db_column='Chemistry', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bookkeeping = models.CharField(db_column='BookKeeping', max_length=5, blank=True, null=True)  # Field name made lowercase.
    commerce = models.CharField(db_column='Commerce', max_length=5, blank=True, null=True)  # Field name made lowercase.
    agriculturalsci = models.CharField(db_column='AgriculturalSci', max_length=5, blank=True, null=True)  # Field name made lowercase.
    electricaldraugting = models.CharField(db_column='ElectricalDraugting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    electricalinstallation = models.CharField(db_column='ElectricalInstallation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    electricalengnsci = models.CharField(db_column='ElectricalEngnSci', max_length=5, blank=True, null=True)  # Field name made lowercase.
    elimuyadinikiislam = models.CharField(db_column='ElimuYaDiniKiislam', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fineart = models.CharField(db_column='FineArt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    arabiclanguage = models.CharField(db_column='ArabicLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    archtecturualdraught = models.CharField(db_column='ArchtecturualDraught', max_length=5, blank=True, null=True)  # Field name made lowercase.
    brickworkmasonary = models.CharField(db_column='BrickworkMasonary', max_length=5, blank=True, null=True)  # Field name made lowercase.
    buildingconstruction = models.CharField(db_column='BuildingConstruction', max_length=5, blank=True, null=True)  # Field name made lowercase.
    carpentryjoinery = models.CharField(db_column='CarpentryJoinery', max_length=5, blank=True, null=True)  # Field name made lowercase.
    engineeringsci = models.CharField(db_column='EngineeringSci', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fittingturning = models.CharField(db_column='FittingTurning', max_length=5, blank=True, null=True)  # Field name made lowercase.
    foodnutrition = models.CharField(db_column='FoodNutrition', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frenchlanguage = models.CharField(db_column='FrenchLanguage', max_length=5, blank=True, null=True)  # Field name made lowercase.
    computerstudies = models.CharField(db_column='ComputerStudies', max_length=5, blank=True, null=True)  # Field name made lowercase.
    plumbing = models.CharField(db_column='Plumbing', max_length=5, blank=True, null=True)  # Field name made lowercase.
    music = models.CharField(db_column='Music', max_length=5, blank=True, null=True)  # Field name made lowercase.
    literatureenglish = models.CharField(db_column='LiteratureEnglish', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mechanicaldraughting = models.CharField(db_column='MechanicalDraughting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    motorvehiclemech = models.CharField(db_column='MotorVehicleMech', max_length=5, blank=True, null=True)  # Field name made lowercase.
    paintingsignwriting = models.CharField(db_column='PaintingSignWriting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    physicaleducation = models.CharField(db_column='PhysicalEducation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    radiotvserving = models.CharField(db_column='RadioTvServing', max_length=5, blank=True, null=True)  # Field name made lowercase.
    surveying = models.CharField(db_column='Surveying', max_length=5, blank=True, null=True)  # Field name made lowercase.
    textiledressmaking = models.CharField(db_column='TextileDressMaking', max_length=5, blank=True, null=True)  # Field name made lowercase.
    theatreart = models.CharField(db_column='TheatreArt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    weldingmetalfabrication = models.CharField(db_column='WeldingMetalFabrication', max_length=5, blank=True, null=True)  # Field name made lowercase.
    workshoptech = models.CharField(db_column='WorkshopTech', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cseeYear2016'


class Cseeyear2016Subjectperformance(models.Model):
    id = models.AutoField(primary_key=True)
    schoolcode = models.CharField(db_column='SchoolCode', max_length=20)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=50)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=7, blank=True, null=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjectgpa = models.CharField(db_column='SubjectGPA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    subjectregranking = models.CharField(db_column='SubjectRegRanking', max_length=5, blank=True, null=True)  # Field name made lowercase.
    subjectnatranking = models.CharField(db_column='SubjectNatRanking', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cseeYear2016SubjectPerformance'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
