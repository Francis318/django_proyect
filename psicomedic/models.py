# Create your models here.
from django.db import models

# Create your models here.

# id -> SERIAL autoincrement
# first_name -> string
# last_name -> string
# generation -> string
# email -> string
# phone -> string
# status -> (activo, dado de baja)
# address -> string
# size -> (s, m, l)
# created_at -> date
# updated_at -> date
# birthdate -> date

# Las clases(modelos) van capitalizadas -> Koder
# Los modelos heredan del modelo predeterminado de Django
# Cada modelo representa una tabla de SQL
# Cada propiedad de la clase(modelo) representa un atributo en la tabla

# LA foreign key se pone en la N en las relaciones 1 - N
# Cuando hay N - N, la FK se pone en el mas chico jerarquicamente -> mentors
#  1 generation - N koders
#  N mentors - N generations
#  1 bootcamp - N generations

#1 paciente- N citas
#N psicologos-N citas
class Citas(models.Model):
    """Generation model."""

    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.pk}, Name:{self.nombre}"


class Psicologo(models.Model):

    first_name = models.CharField(max_length=255)  # -> string
    last_name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # -> En cuanto se cree nos agrega la hora por automatico

    # Foreign keys
    # Related name buena practica -> Nombre del modelo en plural.
    citas = models.ForeignKey(Citas, models.PROTECT, related_name="Psicologos")

    # Representar como nos regresan al koder.
    def __str__(self):
        return f"id: {self.pk}, FirstName -> {self.first_name}, LastName -> {self.last_name}"


class Paciente(models.Model):
    """Mentor model."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    biograpy = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign keys
    citas = models.ManyToManyField(Citas, related_name="Pacientes")

    def __str__(self):
        return f"id: {self.pk}, FirstName {self.first_name}, LastName {self.last_name}"


# Koders pertenece a 1 generacion -> 1 generation - N koderss
# Mentores pertecene a varias generaciones -> N mentors - N generations
# Generaciones pertenecen a un bootcamp -> 1 bootcamp - N generations