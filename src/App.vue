<template>
  <main class="section">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-half">
          <div class="box">
            <h1 class="title has-text-centered">Connexion</h1>

            <form @submit.prevent="handleSubmit" @reset="handleReset">
              <!-- Email -->
              <div class="field">
                <label class="label" for="email">Email</label>
                <div class="control has-icons-left">
                  <input
                    class="input is-info"
                    type="email"
                    id="email"
                    placeholder="Entrez votre email"
                    v-model="email"
                    required
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                </div>
              </div>

              <!-- Password -->
              <div class="field">
                <label class="label" for="password">Mot de passe</label>
                <div class="control has-icons-left">
                  <input
                    class="input is-info"
                    type="password"
                    id="password"
                    placeholder="Entrez votre mot de passe"
                    v-model="password"
                    required
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </div>
              </div>

              <!-- Buttons -->
              <div class="field is-grouped is-grouped-right">
                <p class="control">
                  <button class="button is-info" type="submit">Connexion</button>
                </p>
                <p class="control">
                  <button class="button is-danger" type="reset">Réinitialiser</button>
                </p>
              </div>
            </form>

          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const handleSubmit = () => {
  if (!email.value || !password.value) {
    alert('Veuillez remplir tous les champs.')
  } else {
    console.log('Email :', email.value)
    console.log('Password :', password.value)
    alert('Connexion envoyée !')
  }
}

const handleReset = () => {
  email.value = ''
  password.value = ''
}
</script>
