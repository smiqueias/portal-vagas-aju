from django.db import models
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    contact = models.EmailField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, max_length=200 ,on_delete=models.CASCADE)
    
    OCCUPATION_STATUS = (
        ('E', 'Estágio'),
        ('J', 'Junior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    occupation = models.CharField(
        max_length=1,
        choices=OCCUPATION_STATUS,

    )

    CONTRACT_STATUS = (
        ('PJ', 'PJ'),
        ('CLT', 'CLT')
    )

    contract = models.CharField(
        max_length=3,
        choices=CONTRACT_STATUS

    )

    REMOTE_STATUS = (
        ('S', 'Sim'),
        ('N', 'Não')
    )

    remote = models.CharField(
        max_length=1,
        choices=REMOTE_STATUS
    )

    SALARY_RANGE = (
        ('0-1000', 'R$ 0,00 - R$ 1.000,00'),
        ('1000-3000', 'R$ 1.000,01 - R$ 3.000,00'),
        ('3000-6000', 'R$ 3.000,01 - R$ 6.000,00'),
        ('6000-10000', 'R$ 6.000,01 - R$ 10.000,00'),
        ('10000+', 'R$ 10.000,00 ou mais')
    )

    salary = models.CharField(
        max_length=10,
        choices=SALARY_RANGE,
        blank=True
    )

    STATES_RANGE = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal'),
    )

    states = models.CharField(
        max_length = 2,
        choices = STATES_RANGE,
        blank = True
    )
    

    def __str__(self):
        return self.title

def get_absolute_url(self):
    return reverse("job_detail", args=[str(self.id)])


