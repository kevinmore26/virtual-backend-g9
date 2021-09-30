from django.contrib.auth.models import BaseUserManager

class ManejoUsuarios(BaseUserManager):
    def create_user(self,email,nombre,apellido,tipo,password=None):
        '''Creacion de usuario'''
        if not email:
            raise ValueError('El usuario tiene que tener un correo valido')
        self.normalize_email(email)

        usuarioCreado=self.model(usuarioCorreo=email,usuarioNombre = nombre, usuarioApellido=apellido,usuarioTipo=tipo)

        usuarioCreado.set_password(password)

        usuarioCreado.save(using=self._db)

        return usuarioCreado

    def create_superuser(self,usuarioCorreo,usuarioNombre,usuarioApellido,usuarioTipo,password):
        '''Creacion de un super usuario(administrador)'''
        nuevoUsuario=self.create_user(usuarioCorreo,usuarioNombre,usuarioApellido,usuarioTipo,password)
        
        nuevoUsuario.is_superuser=True
        nuevoUsuario.is_staff=True
        nuevoUsuario.save(using=self._db)
