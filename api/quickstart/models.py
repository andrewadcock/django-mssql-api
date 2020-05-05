# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each OneToOneField has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Annualreport(models.Model):
    # Field name made lowercase.
    annualreportid = models.AutoField(
        db_column='AnnualReportID', primary_key=True)
    # Field name made lowercase.
    reportyear = models.CharField(db_column='ReportYear', max_length=4)

    class Meta:
        managed = False
        db_table = 'AnnualReport'


class Answers(models.Model):
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'Questionelement', models.DO_NOTHING, db_column='ElementID', primary_key=True, related_name="answersElementid")
    # Field name made lowercase.
    statecode = models.OneToOneField(
        'States', models.DO_NOTHING, db_column='StateCode', related_name="answersStatecode")
    # Field name made lowercase.
    programcode = models.OneToOneField(
        'Stateprograms', models.DO_NOTHING, db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Answers'
        unique_together = (('elementid', 'programcode',
                            'statecode', 'statecode', 'year'),)


class AnswersRollover(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(
        db_column='ElementID', blank=True, null=True)
    # Field name made lowercase.
    elementidnew = models.IntegerField(
        db_column='ElementIDNew', blank=True, null=True)
    # Field name made lowercase.
    statecode = models.CharField(
        db_column='StateCode', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    programcode = models.IntegerField(
        db_column='ProgramCode', blank=True, null=True)
    # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)
    updated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Answers_rollover'


class AnswersRollover2(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(
        db_column='ElementID', blank=True, null=True)
    # Field name made lowercase.
    elementidnew = models.IntegerField(
        db_column='ElementIDNew', blank=True, null=True)
    # Field name made lowercase.
    statecode = models.CharField(
        db_column='StateCode', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    programcode = models.IntegerField(
        db_column='ProgramCode', blank=True, null=True)
    # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)
    updated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Answers_rollover2'


class Attachments(models.Model):
    # Field name made lowercase.
    statecode = models.OneToOneField(
        'Stateprograms', models.DO_NOTHING, db_column='StateCode', related_name="attachementsStatecode")
    # Field name made lowercase.
    programcode = models.OneToOneField(
        'Stateprograms', models.DO_NOTHING, db_column='ProgramCode', related_name="attachmentsProgramcode")
    # Field name made lowercase.
    questionid = models.OneToOneField(
        'Questions', models.DO_NOTHING, db_column='QuestionID', blank=True, null=True)
    # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)
    # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=4)
    # Field name made lowercase.
    sectionid = models.OneToOneField(
        'Sections', models.DO_NOTHING, db_column='SectionID')

    class Meta:
        managed = False
        db_table = 'Attachments'


class Certificationinfo(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(
        db_column='StateCode', primary_key=True, max_length=2)
    # Field name made lowercase.
    reportyear = models.CharField(db_column='ReportYear', max_length=4)
    # Field name made lowercase.
    signature = models.CharField(
        db_column='Signature', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    programtype = models.CharField(
        db_column='ProgramType', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    address1 = models.CharField(
        db_column='Address1', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    address2 = models.CharField(
        db_column='Address2', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(
        db_column='State', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    zip = models.CharField(
        db_column='Zip', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    fax = models.CharField(
        db_column='Fax', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    submissiondate = models.DateTimeField(
        db_column='SubmissionDate', blank=True, null=True)
    # Field name made lowercase.
    certificationdate = models.DateTimeField(
        db_column='CertificationDate', blank=True, null=True)
    # Field name made lowercase.
    iscertified = models.BooleanField(
        db_column='IsCertified', blank=True, null=True)
    # Field name made lowercase.
    medicaid = models.BooleanField(db_column='Medicaid')

    class Meta:
        managed = False
        db_table = 'CertificationInfo'
        unique_together = (('statecode', 'reportyear', 'medicaid'),)


class Choicetextlist(models.Model):
    # Field name made lowercase.
    choiceid = models.OneToOneField(
        'Choices', models.DO_NOTHING, db_column='ChoiceID', primary_key=True, related_name="choicetextlistChoiceid")
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'Choices', models.DO_NOTHING, db_column='ElementID')
    # Field name made lowercase.
    questionelementid = models.OneToOneField(
        'Questionelement', models.DO_NOTHING, db_column='QuestionElementID')
    # Field name made lowercase.
    textlistsequence = models.IntegerField(db_column='TextListSequence')
    # Field name made lowercase.
    leadingtext = models.CharField(
        db_column='LeadingText', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    textarearows = models.IntegerField(
        db_column='TextAreaRows', blank=True, null=True)
    # Field name made lowercase.
    textareacols = models.IntegerField(
        db_column='TextAreaCols', blank=True, null=True)
    # Field name made lowercase.
    maxlength = models.IntegerField(
        db_column='MaxLength', blank=True, null=True)
    # Field name made lowercase.
    keepdataonuncheck = models.BooleanField(
        db_column='KeepDataOnUncheck', blank=True, null=True)
    # Field name made lowercase.
    showmaxlength = models.BooleanField(
        db_column='ShowMaxLength', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChoiceTextList'
        unique_together = (('choiceid', 'elementid', 'questionelementid'),)


class Choices(models.Model):
    # Field name made lowercase.
    choiceid = models.IntegerField(db_column='ChoiceID', primary_key=True)
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'Questionelement', models.DO_NOTHING, db_column='ElementID')
    # Field name made lowercase.
    choicetext = models.CharField(db_column='ChoiceText', max_length=5000)
    # Field name made lowercase.
    choicesequence = models.IntegerField(
        db_column='ChoiceSequence', blank=True, null=True)
    # Field name made lowercase.
    explanationtextelementid = models.IntegerField(
        db_column='ExplanationTextElementID', blank=True, null=True)
    # Field name made lowercase.
    reportchoicetext = models.CharField(
        db_column='ReportChoiceText', max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Choices'
        unique_together = (('choiceid', 'elementid'),)


class Choicesdescription(models.Model):
    # Field name made lowercase.
    choiceid = models.IntegerField(db_column='ChoiceID', primary_key=True)
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'Questionelement', models.DO_NOTHING, db_column='ElementID')
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)
    # Field name made lowercase.
    choicetext = models.CharField(
        db_column='ChoiceText', max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChoicesDescription'
        unique_together = (('choiceid', 'elementid', 'startyear'),)


class Fmaprates(models.Model):
    # Field name made lowercase.
    statecode = models.OneToOneField(
        'States', models.DO_NOTHING, db_column='StateCode', primary_key=True)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FMAPRates'
        unique_together = (('statecode', 'fiscalyear'),)


class Fmaprates2(models.Model):
    # Field name made lowercase.
    statecode = models.OneToOneField(
        'States', models.DO_NOTHING, db_column='StateCode', primary_key=True)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FMAPRates2'
        unique_together = (('statecode', 'fiscalyear'),)


class Longanswers(models.Model):
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'Questionelement', models.DO_NOTHING, db_column='ElementID', primary_key=True)
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    # Field name made lowercase. This field type is a guess.
    longanswertext = models.TextField(
        db_column='LongAnswerText', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LongAnswers'
        unique_together = (('elementid', 'statecode', 'programcode', 'year'),)


class Prefilledelementids(models.Model):
    elementid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PreFilledElementIDs'


class PrefilledelementidsBak2010(models.Model):
    elementid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PreFilledElementIDs_bak_2010'


class Questionelement(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID', primary_key=True)
    # Field name made lowercase.
    questionid = models.OneToOneField(
        'Questions', models.DO_NOTHING, db_column='QuestionID', blank=True, null=True)
    # Field name made lowercase.
    questiontypeid = models.OneToOneField(
        'Questiontypes', models.DO_NOTHING, db_column='QuestionTypeID', blank=True, null=True)
    # Field name made lowercase.
    questiontypeid2 = models.OneToOneField(
        'Questiontypes', models.DO_NOTHING, db_column='QuestionTypeID2', blank=True, null=True, related_name="questionelementQuestiontypeid2")
    # Field name made lowercase.
    maxlength = models.IntegerField(
        db_column='MaxLength', blank=True, null=True)
    # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)
    # Field name made lowercase.
    type1description = models.CharField(
        db_column='Type1Description', max_length=225, blank=True, null=True)
    # Field name made lowercase.
    type2description = models.CharField(
        db_column='Type2Description', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    linktoelementid = models.IntegerField(
        db_column='LinkToElementID', blank=True, null=True)
    # Field name made lowercase.
    linktoelementvalue = models.CharField(
        db_column='LinkToElementValue', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    linktoquestiontypeid = models.IntegerField(
        db_column='LinkToQuestionTypeID', blank=True, null=True)
    # Field name made lowercase.
    requiredforcert = models.BooleanField(
        db_column='RequiredForCert', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QuestionElement'


class Questionelementdescription(models.Model):
    # Field name made lowercase.
    elementid = models.OneToOneField(
        Questionelement, models.DO_NOTHING, db_column='ElementID', primary_key=True)
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)
    # Field name made lowercase.
    type1description = models.CharField(
        db_column='Type1Description', max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QuestionElementDescription'
        unique_together = (('elementid', 'startyear'),)


class Questiontypes(models.Model):
    # Field name made lowercase.
    questiontypeid = models.AutoField(
        db_column='QuestionTypeID', primary_key=True)
    # Field name made lowercase.
    questiontypename = models.CharField(
        db_column='QuestionTypeName', max_length=100)

    class Meta:
        managed = False
        db_table = 'QuestionTypes'


class Questions(models.Model):
    # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionID', primary_key=True)
    # Field name made lowercase.
    questionnumber = models.CharField(
        db_column='QuestionNumber', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    questiontext = models.CharField(
        db_column='QuestionText', max_length=5000, blank=True, null=True)
    # Field name made lowercase.
    leadinginstructions = models.CharField(
        db_column='LeadingInstructions', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    sectionid = models.ForeignKey(
        'Sections', models.DO_NOTHING, db_column='SectionID', blank=True, null=True)
    # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)
    # Field name made lowercase.
    acceptattachments = models.BooleanField(
        db_column='AcceptAttachments', blank=True, null=True)
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Questions'


class Requiredforcert(models.Model):
    # Field name made lowercase.
    elementid = models.OneToOneField(
        Questionelement, models.DO_NOTHING, db_column='ElementID', primary_key=True, related_name="requiredforecertElementid")
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RequiredForCert'
        unique_together = (('elementid', 'startyear'),)


class Sectionmedicaid(models.Model):
    # Field name made lowercase.
    sectionid = models.OneToOneField(
        'Sections', models.DO_NOTHING, db_column='SectionID', primary_key=True)
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SectionMedicaid'
        unique_together = (('sectionid', 'startyear'),)


class Sectionstartpage(models.Model):
    # Field name made lowercase.
    sectionid = models.OneToOneField(
        'Sections', models.DO_NOTHING, db_column='SectionID', primary_key=True)
    # Field name made lowercase.
    startpage = models.IntegerField(db_column='StartPage')
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SectionStartPage'
        unique_together = (('sectionid', 'startyear'),)


class Sectiontitle(models.Model):
    # Field name made lowercase.
    sectionid = models.OneToOneField(
        'Sections', models.DO_NOTHING, db_column='SectionID', primary_key=True, related_name="sectiontitleSectionid")
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)
    # Field name made lowercase.
    sectiontitle = models.CharField(
        db_column='SectionTitle', max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SectionTitle'
        unique_together = (('sectionid', 'startyear'),)


class Sections(models.Model):
    # Field name made lowercase.
    sectionid = models.IntegerField(db_column='SectionID', primary_key=True)
    # Field name made lowercase.
    sectiontitle = models.CharField(db_column='SectionTitle', max_length=150)
    # Field name made lowercase.
    issubsection = models.BooleanField(db_column='IsSubsection')
    # Field name made lowercase.
    parentsectionid = models.IntegerField(
        db_column='ParentSectionID', blank=True, null=True)
    # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)
    # Field name made lowercase.
    startyear = models.IntegerField(db_column='StartYear')
    # Field name made lowercase.
    endyear = models.IntegerField(db_column='EndYear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sections'


class Sessionsave(models.Model):
    # Field name made lowercase.
    userid = models.CharField(
        db_column='UserID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    sessionid = models.CharField(
        db_column='SessionID', max_length=36, blank=True, null=True)
    # Field name made lowercase.
    sessioncreation = models.DateTimeField(
        db_column='SessionCreation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SessionSave'


class Stateprograms(models.Model):
    # Field name made lowercase.
    statecode = models.OneToOneField(
        'States', models.DO_NOTHING, db_column='StateCode', related_name="stateprogramsStatecode")
    # Field name made lowercase.
    programcode = models.CharField(
        db_column='ProgramCode', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    programdescription = models.CharField(
        db_column='ProgramDescription', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    startyear = models.CharField(
        db_column='StartYear', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    endyear = models.CharField(
        db_column='EndYear', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    primaryprogram = models.BooleanField(
        db_column='PrimaryProgram', blank=True, null=True)
    # Field name made lowercase.
    medicaid = models.BooleanField(db_column='Medicaid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StatePrograms'
        unique_together = (('statecode', 'programcode'),)


class States(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(
        db_column='StateCode', primary_key=True, max_length=2)
    # Field name made lowercase.
    statename = models.CharField(
        db_column='StateName', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'States'


class Tablecells(models.Model):
    # Field name made lowercase.
    colid = models.AutoField(db_column='ColID', primary_key=True)
    # Field name made lowercase.
    rowid = models.OneToOneField(
        'Tablerows', models.DO_NOTHING, db_column='RowID', blank=True, null=True)
    # Field name made lowercase.
    rowspan = models.IntegerField(db_column='RowSpan', blank=True, null=True)
    # Field name made lowercase.
    colspan = models.IntegerField(db_column='ColSpan', blank=True, null=True)
    # Field name made lowercase.
    headercell = models.BooleanField(db_column='HeaderCell')
    # Field name made lowercase.
    celltext = models.CharField(
        db_column='CellText', max_length=5000, blank=True, null=True)
    # Field name made lowercase.
    embeddedtableid = models.OneToOneField(
        'Tables', models.DO_NOTHING, db_column='EmbeddedTableID', blank=True, null=True)
    # Field name made lowercase.
    choiceid = models.OneToOneField(
        Choices, models.DO_NOTHING, db_column='ChoiceID', blank=True, null=True)
    # Field name made lowercase.
    elementid = models.OneToOneField(
        Questionelement, models.DO_NOTHING, db_column='ElementID', blank=True, null=True)
    # Field name made lowercase.
    textelementorder = models.CharField(
        db_column='TextElementOrder', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TableCells'


class Tablerows(models.Model):
    # Field name made lowercase.
    rowid = models.AutoField(db_column='RowID', primary_key=True)
    # Field name made lowercase.
    tableid = models.OneToOneField(
        'Tables', models.DO_NOTHING, db_column='TableID', blank=True, null=True)
    # Field name made lowercase.
    rowsequence = models.IntegerField(
        db_column='RowSequence', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TableRows'


class Tables(models.Model):
    # Field name made lowercase.
    tableid = models.AutoField(db_column='TableID', primary_key=True)
    # Field name made lowercase.
    tablename = models.CharField(
        db_column='TableName', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    tabletitle = models.CharField(
        db_column='TableTitle', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    border = models.BooleanField(db_column='Border')
    # Field name made lowercase.
    questionid = models.OneToOneField(
        Questions, models.DO_NOTHING, db_column='QuestionID', blank=True, null=True)
    # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)
    # Field name made lowercase.
    isembedded = models.BooleanField(
        db_column='IsEmbedded', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tables'


class Uninsuredchildrenaverages(models.Model):
    # Field name made lowercase.
    statecode = models.OneToOneField(
        States, models.DO_NOTHING, db_column='StateCode', primary_key=True)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages'
        unique_together = (('statecode', 'year', 'linenum'),)


class UninsuredchildrenaveragesBak(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.FloatField(
        db_column='StandardErrorNumber', blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.FloatField(
        db_column='StandardErrorRate', blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak'


class UninsuredchildrenaveragesBak2010(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2010'


class UninsuredchildrenaveragesBak2011(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2011'


class UninsuredchildrenaveragesBak2012(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2012'


class UninsuredchildrenaveragesBak2013(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2013'


class UninsuredchildrenaveragesBak2014(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2014'


class UninsuredchildrenaveragesBak2015(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2015'


class UninsuredchildrenaveragesBak2016(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2016'


class UninsuredchildrenaveragesBak2017(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2017'


class UninsuredchildrenaveragesBak2018(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2018'


class UninsuredchildrenaveragesBak2019(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    linenum = models.IntegerField(db_column='LineNum')
    # Field name made lowercase.
    periodyears = models.CharField(
        db_column='PeriodYears', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    number = models.FloatField(db_column='Number', blank=True, null=True)
    # Field name made lowercase.
    standarderrornumber = models.CharField(
        db_column='StandardErrorNumber', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)
    # Field name made lowercase.
    standarderrorrate = models.CharField(
        db_column='StandardErrorRate', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    asterisktext = models.CharField(
        db_column='AsteriskText', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    asterisktext2 = models.CharField(
        db_column='AsteriskText2', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UninsuredChildrenAverages_bak_2019'


class AnswersBak010912(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_bak_010912'


class AnswersBak012412(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_bak_012412'


class AnswersBak022613(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_bak_022613'


class AnswersBak102814(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_bak_102814'


class AnswersBak110513(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_bak_110513'


class AnswersTemp(models.Model):
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    # Field name made lowercase.
    answertext = models.CharField(
        db_column='AnswerText', max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    answerchoices = models.CharField(
        db_column='AnswerChoices', max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers_temp'


class AuditElementChoices(models.Model):
    audit_datetime = models.DateTimeField(primary_key=True)
    user_id = models.CharField(max_length=15)
    pre_choices = models.CharField(max_length=150, blank=True, null=True)
    post_choices = models.CharField(max_length=150, blank=True, null=True)
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')

    class Meta:
        managed = False
        db_table = 'audit_element_choices'
        unique_together = (('audit_datetime', 'user_id', 'elementid'),)


class AuditElementPostText(models.Model):
    audit_datetime = models.OneToOneField(
        'AuditTableUpdate', models.DO_NOTHING, db_column='audit_datetime', primary_key=True, related_name="auditelementposttextAudit_datetime")
    user = models.OneToOneField('AuditTableUpdate', models.DO_NOTHING)
    post_text = models.CharField(max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'AuditTableUpdate', models.DO_NOTHING, db_column='ElementID', related_name="auditelementposttextElementid")

    class Meta:
        managed = False
        db_table = 'audit_element_post_text'
        unique_together = (('audit_datetime', 'user', 'elementid'),)


class AuditElementPreText(models.Model):
    audit_datetime = models.OneToOneField(
        'AuditTableUpdate', models.DO_NOTHING, db_column='audit_datetime', primary_key=True, related_name="auditelementpretextAudit_datetime")
    user = models.OneToOneField('AuditTableUpdate', models.DO_NOTHING)
    pre_text = models.CharField(max_length=7500, blank=True, null=True)
    # Field name made lowercase.
    elementid = models.OneToOneField(
        'AuditTableUpdate', models.DO_NOTHING, db_column='ElementID', related_name="auditelementpretextElementid")

    class Meta:
        managed = False
        db_table = 'audit_element_pre_text'
        unique_together = (('audit_datetime', 'user', 'elementid'),)


class AuditTableUpdate(models.Model):
    audit_datetime = models.DateTimeField(primary_key=True)
    user_id = models.CharField(max_length=15)
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    programcode = models.IntegerField(db_column='ProgramCode')
    # Field name made lowercase.
    elementid = models.IntegerField(db_column='ElementID')
    audit_type_cd = models.CharField(max_length=2)
    # Field name made lowercase.
    ipaddress = models.CharField(
        db_column='IPAddress', max_length=16, blank=True, null=True)
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audit_table_update'
        unique_together = (('audit_datetime', 'user_id', 'elementid'),)


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class FmapratesBak(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak'


class FmapratesBak2009(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2009'


class FmapratesBak2010(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2010'


class FmapratesBak2011(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2011'


class FmapratesBak2011Wr3731(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2011_WR3731'


class FmapratesBak2012(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2012'


class FmapratesBak2013(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2013'


class FmapratesBak2014(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2014'


class FmapratesBak2015(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2015'


class FmapratesBak2016(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2016'


class FmapratesBak2017(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2017'


class FmapratesBak2018(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2018'


class FmapratesBak2019(models.Model):
    # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=2)
    # Field name made lowercase.
    fiscalyear = models.CharField(db_column='FiscalYear', max_length=4)
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fmaprates_bak_2019'


class Tblsurveyopen(models.Model):
    # Field name made lowercase.
    surveyyear = models.IntegerField(db_column='SurveyYear', primary_key=True)
    # Field name made lowercase.
    opendate = models.DateTimeField(db_column='OpenDate')

    class Meta:
        managed = False
        db_table = 'tblSurveyOpen'
