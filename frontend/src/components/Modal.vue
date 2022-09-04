<template>
  <q-dialog v-model="opened" persistent>
    <q-card style="min-width: 400px">
      <q-card-section class="row items-center q-pb-none">
        <div class="text-h6">Item</div>
        <q-space />
        <q-btn icon="close" flat round dense @click="close" />
      </q-card-section>

      <q-card-section class="q-pa-md">
        <q-form @submit="submit" @reset="resetData" class="q-gutter-md">
          <q-input
            v-model="name"
            label="Nome *"
            :error="!name && !!fieldsErrors.name"
          >
            <template v-slot:error>{{ fieldsErrors.name }}</template>
          </q-input>

          <q-input
            v-model="value"
            label="Valor *"
            type="number"
            :error="!!fieldsErrors.value"
          >
            <template v-slot:error>{{ fieldsErrors.value }}</template>
          </q-input>

          <q-input
            v-model="weight"
            label="Peso *"
            type="number"
            :error="!!fieldsErrors.weight"
          >
            <template v-slot:error>{{ fieldsErrors.weight }}</template>
          </q-input>

          <q-input
            v-model="quantity"
            label="Quantidade *"
            type="number"
            :error="!!fieldsErrors.quantity"
          >
            <template v-slot:error>{{ fieldsErrors.quantity }}</template>
          </q-input>
        </q-form>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="Cancelar" color="negative" @click="close" />

        <q-btn flat label="Salvar" color="primary" @click="submit" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<style></style>

<script>
import { mapGetters, mapActions } from 'vuex';
import { v4 as uuidv4 } from 'uuid';

export default {
  name: 'ItemFormModal',
  props: {
    item: {
      type: Object,
      default: null,
    },
  },
  computed: mapGetters({
    items: 'app/items',
  }),
  data() {
    return {
      edit: false,
      opened: false,
      id: null,
      name: '',
      value: '',
      weight: '',
      quantity: '',
      fieldsErrors: {},
    };
  },
  methods: {
    ...mapActions({
      addItem: 'app/addItem',
      editItem: 'app/editItem',
    }),
    open(item = null) {
      this.edit = !!item;
      this.opened = true;

      if (this.edit) {
        const { id, name, value, quantity, weight } = item;

        this.id = id;
        this.name = name;
        this.value = value;
        this.weight = weight;
        this.quantity = quantity;
      }
    },
    close() {
      this.resetData();

      this.opened = false;
    },
    isValidInteger(value) {
      return (
        !Number.isNaN(parseInt(value, 10)) ||
        value.toString().includes('.') ||
        value.toString().includes(',')
      );
    },
    isValidFloat(value) {
      return !Number.isNaN(parseFloat(value));
    },
    validateFields() {
      const newErrors = {};

      if (!this.name) newErrors.name = 'O nome é obrigatório';

      if (!this.isValidFloat(this.value))
        newErrors.value = 'O valor é obrigatório e deve ser um número decimal';

      if (!this.isValidInteger(this.weight)) {
        newErrors.weight = 'O peso é inválido, é esperado um número inteiro';
      }

      if (!this.isValidInteger(this.quantity)) {
        newErrors.quantity =
          'A quantidade é inválida, é esperado um número inteiro';
      }

      this.fieldsErrors = { ...newErrors };

      return Object.keys(newErrors).length === 0;
    },
    submit() {
      if (!this.validateFields()) return;

      const newItem = {
        name: this.name,
        value: this.value,
        weight: this.weight,
        quantity: this.quantity,
      };

      if (this.edit) {
        this.editItem({ itemId: this.id, data: newItem });
      } else {
        this.addItem({ ...newItem, id: uuidv4() });
      }

      this.close();
    },
    resetData() {
      this.edit = false;
      this.id = null;
      this.name = '';
      this.value = '';
      this.weight = '';
      this.quantity = '';
      this.fieldsErrors = {};
    },
  },
};
</script>
