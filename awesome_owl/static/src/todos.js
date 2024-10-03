/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
export class TodoItem extends Component {
  static template = "my_module.TodoItem";
  static props = {
    todo: {
      type: Object,
      shape: {
        id: Number,
        description: { type: String },
        isCompleted: Boolean,
      }
    },
  };
}

export class TodoList extends Component {
  static template = "my_module.TodoList";
  static components = { TodoItem };
  setup() {
    this.todos = useState([
      { id: 1, description: "qqq", isCompleted: false },
      { id: 2, description: "www", isCompleted: false },
      { id: 3, description: "buy milk", isCompleted: false },
    ]);
  }
}