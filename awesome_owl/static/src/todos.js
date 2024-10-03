/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useAutoFocus } from "./utils";

export class TodoItem extends Component {
  static template = "my_module.TodoItem";
  static props = {
    todo: {
      type: Object,
      shape: {
        id: Number,
        description: { type: String },
        isCompleted: Boolean,
      },
    },
    toggleTodo: Function,
    removeTodo: Function,
  };
  // setup() {
  //   markCompleted = useState(props.todo.isCompleted);
  // }
  onChange() {
    this.props.toggleTodo(this.props.todo.id);
  }
  onRemove() {
    this.props.removeTodo(this.props.todo.id);
  }
}

export class TodoList extends Component {
  static template = "my_module.TodoList";
  static components = { TodoItem };
  setup() {
    this.inputRef = useAutoFocus("qqq");
    this.state = useState({ version: 0 });
    this.todos = useState([
      { id: 1, description: "qqq", isCompleted: false },
      { id: 2, description: "www", isCompleted: false },
      { id: 3, description: "buy milk", isCompleted: true },
    ]);
  }
  cnt = 3;
  increment() {
    this.state.version++;
  }
  addTodo(ev) {
    // debugger;
    if (ev.keyCode !== 13) return;
    const description = ev.target.value.trim();
    if (!description) return;
    const newItem = { id: ++this.cnt, description, isCompleted: false };
    this.todos.push(newItem);
  }
  toggleTodo(id) {
    const item = this.todos.find(q => q.id === id);
    item.isCompleted = !item.isCompleted;
  }
  removeTodo(id) {
    const idx = this.todos.findIndex(q => q.id === id);
    if (idx >= 0) {
      this.todos.splice(idx, 1);
    }
  }
}