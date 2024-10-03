/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class Card extends Component {
  static template = "my_module.Card";

  setup() {
    this.isOpen = useState({ value: true });
  }

  toggle() {
    this.isOpen.value = !this.isOpen.value;
  }
  // increment() {
  //   this.state.value++;
  // }
}