import { Notify } from 'quasar';
import { get, post, httpDelete, patch } from '../../service/api';

export const getItems = async ({ commit }) => {
  try {
    const response = await get('/items');

    commit('setItems', response);
  } catch {
    Notify.create({
      message: 'Falha ao buscar os itens',
      type: 'negative',
      position: 'top-right',
    });
  }
};

export const addItem = async ({ dispatch }, item) => {
  try {
    await post('/items', item);

    dispatch('getItems');

    Notify.create({
      message: 'Item adicionado com sucesso!',
      type: 'positive',
      position: 'top-right',
    });
  } catch {
    Notify.create({
      message: 'Falha ao cadastrar o item',
      type: 'negative',
      position: 'top-right',
    });
  }
};

export const removeItem = async ({ dispatch }, itemId) => {
  try {
    await httpDelete(`/items/${itemId}`);

    dispatch('getItems');

    Notify.create({
      message: 'Item removido com sucesso!',
      type: 'positive',
      position: 'top-right',
    });
  } catch {
    Notify.create({
      message: 'Falha ao remover o item',
      type: 'negative',
      position: 'top-right',
    });
  }
};

export const editItem = async ({ dispatch }, { itemId, data }) => {
  try {
    await patch(`/items/${itemId}`, data);

    dispatch('getItems');

    Notify.create({
      message: 'Item editado com sucesso!',
      type: 'positive',
      position: 'top-right',
    });
  } catch {
    Notify.create({
      message: 'Falha ao editar o item',
      type: 'negative',
      position: 'top-right',
    });
  }
};

// export const deleteAll = ({ commit }) => {
//   commit('setItems', []);
// };

export const assembleKnapsack = async (data) => {
  try {
    return await patch('/knapsack', data);
  } catch {
    Notify.create({
      message: 'Falha ao montar a mochila',
      type: 'negative',
      position: 'top-right',
    });

    return null;
  }
};
