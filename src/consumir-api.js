import { Axios } from "axios"
new Vue({
	el: '#app',
	data(){
		return {
			usuarios: [],
			cantidadResultados: 5
		}
	},
	methods: {
		leerAPI(){
			axios.get('https://reqres.in/api/users', {
				params: {
					'per_page': this.cantidadResultados
				}
			}).then(response => {
				this.usuarios = response.data.data
			}).catch(e => {
				console.log(e)
			})
		}
	},
	created(){
		this.leerAPI()
	}
})