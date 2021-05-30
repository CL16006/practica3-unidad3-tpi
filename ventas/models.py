from django.db import models

class categoria(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ${} {}'.format(self.nombre,self.precio,self.categoria)

class ventas(models.Model):
    descripcion = models.CharField(max_length=200)
    producto=models.ForeignKey(productos,on_delete=models.CASCADE)
    fecha=models.DateTimeField()

    def __str__(self):
        return self.descripcion


