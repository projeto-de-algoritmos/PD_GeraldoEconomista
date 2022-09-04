<template>
  <q-page>
    <FormModal ref="formModal" />

    <div class="page-container flex column q-mt-xl q-mx-auto">
      <q-table
        title="Itens"
        :data="items"
        row-key="name"
        :columns="columns"
        :pagination.sync="pagination"
        no-data-label="Nenhum item cadastrada"
      >
        <template v-slot:top-right>
          <q-btn
            no-caps
            color="positive"
            class="q-mr-md"
            icon-right="backpack"
            @click="() => $router.push({ name: 'Knapsack' })"
          >
            <q-tooltip>Montar mochila</q-tooltip>
          </q-btn>

          <q-btn
            color="negative"
            icon-right="delete_forever"
            no-caps
            @click="deleteAll"
          >
            <q-tooltip>Apagar todos os itens</q-tooltip>
          </q-btn>

          <q-btn
            color="primary"
            icon-right="add"
            no-caps
            class="q-ml-md"
            @click="() => openModal()"
          >
            <q-tooltip>Adicionar novo item</q-tooltip>
          </q-btn>
        </template>

        <template v-slot:body-cell-actions="props">
          <q-td :props="props">
            <q-btn
              color="primary"
              icon-right="edit"
              no-caps
              flat
              dense
              @click="() => openModal(props.row)"
            >
              <q-tooltip>Editar este item</q-tooltip>
            </q-btn>

            <q-btn
              color="negative"
              icon-right="delete"
              no-caps
              flat
              dense
              @click="deleteItem(props.row.id)"
            >
              <q-tooltip>Remover este item</q-tooltip>
            </q-btn>
          </q-td>
        </template>

        <template v-slot:no-data="{ icon, message }">
          <div
            class="full-width row flex-center q-gutter-sm"
            style="color: #ff00ff"
          >
            <q-icon size="2em" name="sentiment_dissatisfied" />

            <span> {{ message }} </span>

            <q-icon size="2em" :name="icon" />
          </div>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<style>
.page-container {
  width: 80%;
}
</style>

<script>
import { mapGetters, mapActions } from 'vuex';

import FormModal from 'components/Modal.vue';

export default {
  name: 'PageIndex',
  components: {
    FormModal,
  },
  mounted() {
    this.$q.lang.table.recordsPerPage = 'Registros por páginas';

    this.$q.lang.table.pagination = (start, end, total) => {
      return `${start}-${end} de ${total}`;
    };
  },
  computed: mapGetters({
    items: 'app/items',
  }),
  data() {
    return {
      pagination: {
        rowsPerPage: 10,
      },
      columns: [
        {
          name: 'name',
          label: 'Nome',
          align: 'left',
          required: true,
          field: 'name',
        },
        {
          name: 'value',
          label: 'Valor',
          align: 'left',
          required: true,
          field: 'value',
        },
        {
          name: 'weight',
          label: 'Peso',
          align: 'left',
          required: true,
          field: 'weight',
        },
        {
          name: 'quantity',
          label: 'Quantidade',
          align: 'left',
          required: true,
          field: 'quantity',
        },
        { name: 'actions', label: 'Ações', align: 'right' },
      ],
    };
  },
  methods: {
    ...mapActions({
      addItem: 'app/addItem',
      editItem: 'app/editItem',
      removeItem: 'app/removeItem',
      deleteAll: 'app/deleteAll',
    }),
    openModal(item = null) {
      this.$refs.formModal.open(item);
    },
    deleteItem(itemId) {
      this.$q
        .dialog({
          title: 'Confirmação',
          message: 'Você tem certeza que deseja apagar este item?',
          cancel: {
            flat: true,
            color: 'negative',
            label: 'Cancelar',
          },
          persistent: true,
        })
        .onOk(() => {
          this.removeItem(itemId);
        });
    },
  },
};
</script>
