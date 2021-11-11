<template>
  <div class="container">
    <div class="row">
      <div class="col m12 card-panel">
        <form @submit.prevent = "agregarUsuario">
            <div class="row">
              <div class="col m4">
                <label>Nombre</label>
                <input type="text" v-model="nombre">
              </div>
              <div class="col m4">
                <label>Apellido</label>
                <input type="text" v-model="apellido">
              </div>
            </div>
          <div class="row">
            <div class="col m4">
              <label>Edad</label>
              <input type="number" v-model="edad">
            </div>
            <div class="col m4">
              <label>Estado Civil</label>
              <select v-model="estado_civil">
                <option value="">Seleccione</option>
                <option value="C">Casado</option>
                <option value="S">Soltero</option>
                <option value="D">Divorciado</option>
                <option value="V">Viudo</option>
              </select>
            </div>
            <div class="col m4">
              <label>Correo</label>
            <input type="email" v-model="correo">
            </div>
          </div>
          
          <div class="row">
            <form @submit.prevent="agregarPasatiempo">
              <div class="col m4 card-panel">
                <label>Pasatiempo</label>
                <input type="text" v-model="pasatiempo">
                <button type="submit" class="btn indigo darken-3">AGREGAR PASATIEMPO <i class="material-icons right">send</i></button>
                <br>
                <ul>
                  <li v-for="pasatiempo in pasatiempos" v-bind:key="pasatiempo">
                      {{pasatiempo.id}} - {{pasatiempo.descripcion}}
                      <a href="#!"><i class="material-icons">close</i></a>
                  </li>
                </ul>
              </div>
            </form>
          </div>

          <div class="row">
            <div class="col m4">
              <label><input type="checkbox" v-model="suscrito"><span>suscribirse al boletin de noticias.</span></label>
            </div>
          </div>

          <div class="row">
            <button type="submit" class="btn indigo darken-4">AGREGAR USUARIO <i class="material-icons right">add_circle</i></button>
          </div>
        </form> 
      </div>
    </div>

    <div class="row">
      <div class="col m12">
        <table class="table bordered striped">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>Edad</th>
              <th>Estado Civil</th>
              <th>Correo</th>
              <th>Pasatiempos</th>
              <th>Suscrito</th>
              <th>Editar</th>
              <th>Eliminar</th>
            </tr>
          </thead>
          <tbody>
              <tr v-for="usuario in usuarios" v-bind:key="usuario">
                <td>{{usuario.nombre}}</td>
                <td>{{usuario.apellido}}</td>
                <td>{{usuario.edad}}</td>
                <td>{{usuario.estado_civil}}</td>
                <td>{{usuario.correo}}</td>
                <td>
                  <ul>
                    <li v-for="pasatiempo in usuario.pasatiempos" v-bind:key="pasatiempo">{{pasatiempo.id}} - {{pasatiempo.descripcion}}</li>
                  </ul>
                </td>
                <td><label><input type="checkbox" disabled v-model="usuario.suscrito"><span></span></label></td>
                <td><a href="#!"><i class="material-icons">create</i></a></td>
                <td><a href="#!"><i class="material-icons">delete</i></a></td>
              </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import M from 'materialize-css'
export default {
  name: 'App',
  data(){
    return {
      nombre: '',
      apellido: '',
      edad: 0,
      estado_civil: '',
      correo: '',
      suscrito: false,
      pasatiempo: '',
      pasatiempos: [],
      usuarios: [],

      select_instances: []
    }
  },
  mounted()
  {
    var elems = document.querySelectorAll('select');
    this.select_instances = M.FormSelect.init(elems, null);
  },
  methods: {
    agregarUsuario()
    {
        var data = {
          nombre: this.nombre,
          apellido: this.apellido,
          edad: this.edad,
          estado_civil: this.estado_civil,
          correo: this.correo,
          suscrito: this.suscrito,
          pasatiempos: this.pasatiempos
        };
        this.usuarios.push(data);
        this.nombre = '';
        this.apellido = '';
        this.edad = 0;
        this.estado_civil = '';
        this.correo = '';
        this.suscrito = false;
        this.pasatiempo = '';
        this.pasatiempos = [];
    },
    agregarPasatiempo()
    {
      var total = this.pasatiempos.length;
      var ultimo = 0;
      if(total > 0)
      {
        ultimo = this.pasatiempos[total - 1].id;
      }
      var data = {
        id: ultimo + 1,
        descripcion: this.pasatiempo
      };
      this.pasatiempos.push(data);
      this.pasatiempo = '';
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
