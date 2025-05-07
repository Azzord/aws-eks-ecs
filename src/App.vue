<template>
  <main class="section">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-half">
          <div class="box">
            <!-- Onglets -->
            <div class="tabs is-centered is-toggle is-toggle-rounded mb-4">
              <ul>
                <li :class="{ 'is-active': mode === 'login' }">
                  <a @click="mode = 'login'">Connexion</a>
                </li>
                <li :class="{ 'is-active': mode === 'register' }">
                  <a @click="mode = 'register'">S'enregistrer</a>
                </li>
              </ul>
            </div>

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
                  <span class="icon is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                </div>
              </div>

              <!-- Mot de passe -->
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
                  <span class="icon is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </div>
              </div>

              <!-- Confirmation mot de passe (seulement en register) -->
              <div
                v-if="mode === 'register'"
                class="field"
              >
                <label class="label" for="confirmPassword">Confirmer le mot de passe</label>
                <div class="control has-icons-left">
                  <input
                    class="input"
                    :class="{ 'is-danger': passwordMismatch }"
                    type="password"
                    id="confirmPassword"
                    placeholder="Confirmez le mot de passe"
                    v-model="confirmPassword"
                    required
                  />
                  <span class="icon is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </div>
                <p v-if="passwordMismatch" class="help is-danger">
                  Les mots de passe ne correspondent pas.
                </p>
              </div>

              <!-- Boutons -->
              <div class="field is-grouped is-grouped-right">
                <p class="control">
                  <button class="button is-info" type="submit">
                    {{ mode === 'login' ? 'Connexion' : "S'inscrire" }}
                  </button>
                </p>
                <p class="control">
                  <button class="button is-light" type="reset">Réinitialiser</button>
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
import { ref, computed } from 'vue'

const mode = ref('login') // 'login' ou 'register'
const email = ref('')
const password = ref('')
const confirmPassword = ref('')

const passwordMismatch = computed(() => {
  return mode.value === 'register' && password.value !== confirmPassword.value
})

const handleSubmit = () => {
  if (mode.value === 'register' && passwordMismatch.value) {
    alert('Les mots de passe ne correspondent pas.')
    return
  }

  if (!email.value || !password.value) {
    alert('Veuillez remplir tous les champs.')
    return
  }

  alert(
    mode.value === 'login'
      ? `Tentative de connexion pour ${email.value}`
      : `Tentative d'inscription pour ${email.value}`
  )
}

const handleReset = () => {
  email.value = ''
  password.value = ''
  confirmPassword.value = ''
}
</script>

<style>
/* Icônes Font Awesome */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
</style>
