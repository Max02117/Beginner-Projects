<template>
    <div>
      <h2>Регистрация</h2>
      <form @submit.prevent="register">
        <div>
          <label for="registerName">Имя:</label>
          <input type="text" id="registerName" v-model="registerName" />
        </div>
        <div>
          <label for="registerAge">Возраст:</label>
          <input type="number" id="registerAge" v-model.number="registerAge" />
        </div>
        <button type="submit">Зарегистрироваться</button>
      </form>
  
      <!-- Сообщение после регистрации -->
      <p v-if="registerMessage" :style="{ color: registerError ? 'red' : 'green' }">
        {{ registerMessage }}
      </p>
  
      <!-- Если локально авторизован — показываем приветствие и кнопку "Выйти" -->
      <div v-if="authenticated" class="welcome">
        <p>Вы авторизованы. Здравствуйте, <strong>{{ loggedUserName }}</strong> (ID: {{ loggedUserId }})</p>
        <button @click="logout">Выйти</button>
      </div>
  
      <!-- Форма логина -->
      <div v-else>
        <h2>Авторизация</h2>
        <form @submit.prevent="login">
          <div>
            <label for="loginId">Введите ID:</label>
            <input type="number" id="loginId" v-model.number="loginId" />
          </div>
          <button type="submit">Авторизоваться</button>
        </form>
  
        <!-- Cообщение об ошибке при логине -->
        <p v-if="loginMessage && !loginSuccess" style="color: red;">{{ loginMessage }}</p>

        <!-- Модал-подтверждение -->
        <div v-if="loginSuccess" class="modal">
          <div class="modal-content">
            <p>Авторизация успешна! Найден пользователь: <strong>{{ loggedUserName }}</strong> (ID: {{ loggedUserId }})</p>
            <div class="modal-actions">
              <!-- Вместо эмита в родителя — локальная авторизация -->
              <button @click="confirmLocalAuth">Продолжить</button>
              <button @click="goBack">Вернуться</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'AuthComponent',
    data() {
      return {
        // регистрация
        registerName: '',
        registerAge: null,
        registerMessage: '',
        registerError: false,
        registeredUserId: null,
  
        // логин по id
        loginId: null,
        loginMessage: '',
        loginSuccess: false,
        loggedUserId: null,
        loggedUserName: null,
  
        // локальная метка авторизации
        authenticated: false
      }
    },
  
    methods: {
      async register() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/users/', {
            name: this.registerName,
            age: Number(this.registerAge)
          });
  
          this.registeredUserId = response.data.id;
          this.registerMessage = `Регистрация успешна! Ваш ID: ${this.registeredUserId}`;
          this.registerError = false;
  
          // Очистка полей формы
          this.registerName = '';
          this.registerAge = null;
        } catch (err) {
          console.error(err);
          this.registerError = true;
          this.registerMessage = 'Ошибка регистрации: ' + (err.response?.data?.detail || err.message);
        }
      },
  
      async login() {
        // Валидация ввода
        if (this.loginId === null || this.loginId === '') {
          this.loginMessage = 'Введите числовой ID';
          this.loginSuccess = false;
          return;
        }
  
        try {
          const response = await axios.get(`http://127.0.0.1:8000/users/${this.loginId}`);
          // сохраняем данные пользователя для показа и показываем модалку подтверждения
          this.loggedUserId = response.data.id;
          this.loggedUserName = response.data.name ?? '';
          this.loginMessage = '';
          this.loginSuccess = true; // показывает модальное окно
        } catch (err) {
          console.error(err);
          this.loginSuccess = false;
          this.loginMessage = err.response?.status === 404
            ? 'Пользователь не найден'
            : ('Ошибка авторизации: ' + (err.response?.data?.detail || err.message));
        }
      },
  
      // Нажатие "Продолжить"
      confirmLocalAuth() {
        // ставим флаг, чтобы показать приветствие в том же компоненте
        this.authenticated = true;
        // закрываем модалку
        this.loginSuccess = false;
        // очищаем сообщение/поле логина по желанию
        this.loginMessage = '';
        this.loginId = null;
      },
  
      // Закрыть модалку и вернуться к форме (не авторизовывая)
      goBack() {
        this.loginSuccess = false;
        this.loginMessage = '';
        // не очищаем loggedUser* чтобы можно было видеть данные в модалке
      },
  
      // Кнопка "Выйти"
      logout() {
        this.authenticated = false;
        this.loggedUserId = null;
        this.loggedUserName = null;
      }
    }
  }
  </script>
  
  <style scoped>
  /* простая стилизация */
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display:flex;
    align-items:center;
    justify-content:center;
    background: rgba(0,0,0,0.4);
    z-index: 1000;
  }
  
  .modal-content {
    background: #fff;
    padding: 16px;
    border-radius: 8px;
    min-width: 260px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }
  
  .modal-actions {
    margin-top: 12px;
    display:flex;
    gap: 8px;
    justify-content:center;
  }
  
  .welcome {
    margin-top: 12px;
    padding: 12px;
    background: #f0f9f0;
    border: 1px solid #dfeedd;
    border-radius: 6px;
  }
  </style>