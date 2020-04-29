# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Sections(models.Model):
    sectionid = models.IntegerField(db_column='SectionID', primary_key=True)  # Field name made lowercase.
    sectiontitle = models.CharField(db_column='SectionTitle', max_length=150)  # Field name made lowercase.
    issubsection = models.BooleanField(db_column='IsSubsection')  # Field name made lowercase.
    parentsectionid = models.IntegerField(db_column='ParentSectionID', blank=True, null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')  # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sections'


class Answers(models.Model):
    elementid = models.ForeignKey('Questionelement', models.DO_NOTHING, db_column='ElementID', primary_key=True)  # Field name made lowercase.
    statecode = models.ForeignKey('States', models.DO_NOTHING, db_column='StateCode')  # Field name made lowercase.
    programcode = models.ForeignKey('Stateprograms', models.DO_NOTHING, db_column='ProgramCode')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    answertext = models.CharField(db_column='AnswerText', max_length=7500, blank=True, null=True)  # Field name made lowercase.
    answerchoices = models.CharField(db_column='AnswerChoices', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Answers'
        unique_together = (('elementid', 'programcode', 'statecode', 'statecode', 'year'),)
        unique_together = (('year'),)


class Questions(models.Model):
    questionid = models.IntegerField(db_column='QuestionID', primary_key=True)  # Field name made lowercase.
    questionnumber = models.CharField(db_column='QuestionNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    questiontext = models.CharField(db_column='QuestionText', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    leadinginstructions = models.CharField(db_column='LeadingInstructions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sectionid = models.ForeignKey('Sections', models.DO_NOTHING, db_column='SectionID', blank=True, null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    acceptattachments = models.BooleanField(db_column='AcceptAttachments', blank=True, null=True)  # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')  # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions'

class Questionelement(models.Model):
    elementid = models.IntegerField(db_column='ElementID', primary_key=True)  # Field name made lowercase.
    questionid = models.ForeignKey('Questions', models.DO_NOTHING, db_column='QuestionID', blank=True, null=True)  # Field name made lowercase.
    # questiontypeid = models.ForeignKey('Questiontypes', models.DO_NOTHING, db_column='QuestionTypeID', blank=True, null=True)  # Field name made lowercase.
    # questiontypeid2 = models.ForeignKey('Questiontypes', models.DO_NOTHING, db_column='QuestionTypeID2', blank=True, null=True)  # Field name made lowercase.
    maxlength = models.IntegerField(db_column='MaxLength', blank=True, null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')  # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)  # Field name made lowercase.
    type1description = models.CharField(db_column='Type1Description', max_length=225, blank=True, null=True)  # Field name made lowercase.
    type2description = models.CharField(db_column='Type2Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    linktoelementid = models.IntegerField(db_column='LinkToElementID', blank=True, null=True)  # Field name made lowercase.
    linktoelementvalue = models.CharField(db_column='LinkToElementValue', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linktoquestiontypeid = models.IntegerField(db_column='LinkToQuestionTypeID', blank=True, null=True)  # Field name made lowercase.
    requiredforcert = models.BooleanField(db_column='RequiredForCert', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionElement'

class States(models.Model):
    statecode = models.CharField(db_column='StateCode', primary_key=True, max_length=2)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'States'
    
    def __str__(self):
       return statename

class Stateprograms(models.Model):
    statecode = models.ForeignKey('States', models.DO_NOTHING, db_column='StateCode')  # Field name made lowercase.
    programcode = models.AutoField(db_column='ProgramCode', primary_key=True)  # Field name made lowercase.
    programdescription = models.CharField(db_column='ProgramDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    startyear = models.CharField(db_column='StartYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    endyear = models.CharField(db_column='EndYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    primaryprogram = models.BooleanField(db_column='PrimaryProgram', blank=True, null=True)  # Field name made lowercase.
    medicaid = models.BooleanField(db_column='Medicaid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatePrograms'
        unique_together = (('statecode', 'programcode'),)

