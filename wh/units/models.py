from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Unit(models.Model):
	name			= models.CharField(null = False, max_length=100, unique=True)

	faction			= models.CharField(
		null = False,
        max_length = 3,
        choices	= [
	        ('AA', 'Adeptus Astartes'),
	        ('AS', 'Adepta Sororitas'),
	        ('AC', 'Adeptus Custodes'),
	        ('AM', 'Adeptus Mechanicus'),
	        ('IK', 'Imperial Knights'),
	        ('HA', 'Heretic Astartes'),
	        ('CD', 'Chaos Daemons'),
	        ('CK', 'Chaos Knights'),
	        ('IA', 'Imperial Agents'),
	        ('IG', 'Imperial Guard'),
	        ('GC', 'Genestealer Cults'),
	        ('T', 'Tyranids'),
	        ('E', 'Eldar'),
	        ('DE', 'Dark Eldar'),
	        ('H', 'Harlequins'),
	        ('N', 'Necrons'),
	        ('O', 'Orks'),
	        ('TE', 'Tau Empire'),	        
	    ]
    )

	weapon_skill 	= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	ballistic_skill = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	strength 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	toughness 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	wounds 			= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	attacks 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	leadership 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	armor_save 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

	total_model_count		= models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

	leader 					= models.BooleanField(null=False, default=False)

	leader_name				= models.CharField(blank=True, max_length=100)
	leader_weapon_skill 	= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	leader_ballistic_skill 	= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
	leader_strength 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	leader_toughness 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	leader_wounds 			= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	leader_attacks 			= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	leader_leadership 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
	leader_armor_save 		= models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])	