from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Boot(models.Model):
    kmdt_name = models.CharField(max_length=25, verbose_name="commander name")
    LTZS = "Lt.z.S"
    OLTZS = "Olt.z.S"
    KPTLT = "KptLt"
    KKPT = "KKpt"
    RANK_CHOICES = ((LTZS, "Lt.z.S"), (OLTZS, "Olt.z.S"), (KPTLT, "KptLt"), (KKPT, "KKpt"))
    kmdt_rank = models.CharField(max_length=10, choices=RANK_CHOICES, verbose_name="commander rank")
    bt_name = models.CharField(max_length=4, verbose_name="vessel name")
    U = "U"
    UB = "UB"
    UC = "UC"
    CLASS_CHOICES = ((U, "U"), (UB, "UB"), (UC, "UC"))
    bt_class = models.CharField(max_length=10, choices=CLASS_CHOICES, verbose_name="uboot class")
    GREEN = "Green"
    TRAINED = "Trained"
    VETERAN  = "Veteran"
    ELITE = "Elite"
    CREW_CHOICES = ((GREEN, "Green"), (TRAINED, "Trained"), (VETERAN, "Veteran"), (ELITE, "Elite"))
    crew_quality = models.CharField(default=1, max_length=10, choices=CREW_CHOICES, verbose_name="crew quality")
    C06 = "C/06"
    G6 = "G/6"
    C35 = "C35/91"
    NA = "N/A"
    SMALL = "3.7cm"
    MEDIUM = "8.8cm"
    LARGE  = "10.5cm"
    XLARGE = "15cm"
    TORP_CHOICES = ((NA, "N/A"), (C06, "C/06"), (G6, "G/6"), (C35, "C35/91"))
    GUN_CHOICES = ((SMALL, "3.7cm"), (MEDIUM, "8.8cm"), (LARGE, "10.5cm"), (XLARGE, "15cm"))
    deck_gun = models.CharField(default=0, max_length=10, choices=GUN_CHOICES, verbose_name="deck gun")
    fwd_torp_tube1 = models.CharField(default=1, max_length=10, choices=TORP_CHOICES, verbose_name="fwd torp tube 1")
    fwd_torp_tube2 = models.CharField(default=1, max_length=10, choices=TORP_CHOICES, verbose_name="fwd torp tube 2")
    fwd_torp_tube3 = models.CharField(default=1, max_length=10, choices=TORP_CHOICES, verbose_name="fwd torp tube 3")
    fwd_torp_tube4 = models.CharField(default=1, max_length=10, choices=TORP_CHOICES, verbose_name="fwd torp tube 4")
    fwd_c35_reloads = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)], verbose_name="fwd C35/91 reloads")
    fwd_c06_reloads = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)], verbose_name="fwd C/06 reloads")
    fwd_g6_reloads = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)], verbose_name="fwd G/6 reloads")
    aft_torp_tube1 = models.CharField(default=1, max_length=10, choices=TORP_CHOICES, verbose_name="aft torp tube 1")
    aft_torp_tube2 = models.CharField(default=1, max_length=10, choices=TORP_CHOICES, verbose_name="aft torp tube 2")
    aft_c35_reloads = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)], verbose_name="aft C35/91 reloads")
    aft_c06_reloads = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)], verbose_name="aft C/06 reloads")
    aft_g6_reloads = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(12)], verbose_name="aft G/6 reloads")
    gun_damage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="gun damage")
    hull_damage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)], verbose_name="hull damage")
    flooding = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)], verbose_name="flooding")
    periscope = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="periscope")
    wireless = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="wireless")
    hydro_phones = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="hydro phones")
    batteries = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)], verbose_name="batteries")
    fwd_torp_door = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="fwd torp door")
    aft_torp_door = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="aft torp door")
    fuel_tanks = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="fuel tanks")
    dive_planes = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name="dive planes")
    LW = "LW"
    SW = "SW"
    KIA = "KIA"
    WOUND_CHOICES = ((NA, "N/A"), (LW, "LW"), (SW, "SW"), (KIA, "KIA"))
    kmdt_wound = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="Commander wounds")
    wound_1wo = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="1st Officer wounds")
    wound_2wo = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="2nd Officer wounds")
    li_wound = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="Engineer wounds")
    doctor_wound = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="Doctor wounds")
    crew_wound_1 = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="1st crew wounds")
    crew_wound_2 = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="2nd crew wounds")
    crew_wound_3 = models.CharField(default=0, max_length=10, choices=WOUND_CHOICES, verbose_name="3rd crew wounds")
    tonnage_sunk = models.IntegerField(default=0, verbose_name="tonnage sunk")
    active = models.BooleanField(default=True)
    def __str__(self):
        return str(self.kmdt_name) + " | " + str(self.bt_name)
