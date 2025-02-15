from django.db import models

class HealthProfessional(models.Model):
    id = models.AutoField(primary_key=True, db_column="HealthProfessionalId")
    full_name = models.CharField(max_length=255, db_column="TrandingName")
    social_name = models.CharField(max_length=255, blank=True, null=True, db_column="SocialName")
    profession = models.CharField(max_length=100, db_column="Profession")
    zipcode = models.CharField(max_length=10, db_column="ZipCode") 
    adress_street = models.TextField(max_length=255, db_column="AddressStreet")
    adress_neighborhood = models.TextField(max_length=255, db_column="AddressNeighborhood")
    city = models.CharField(max_length=100, db_column="City") 
    state = models.CharField(max_length=100, db_column="State")
    phone = models.CharField(max_length=20, db_column="Phone")
    email = models.EmailField(max_length=100, db_column="Email")

    created_at = models.DateTimeField(auto_now_add=True, db_column="CreationDate")
    updated_at = models.DateTimeField(auto_now=True, db_column="UpdateDate")
    deleted_at = models.DateTimeField(null=True, blank=True, db_column="DeletionDate")

    def __str__(self):
        return self.social_name if self.social_name else self.full_name