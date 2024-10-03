/** @odoo-module */

import { useRef, onMounted, useEffect } from "@odoo/owl";

export function useAutoFocus(name) {
  const ref = useRef(name);
  useEffect(
    (el) => {
      // console.log('useAutoFocus', el);
      if (el) {
        el.focus();
        // console.log(name, "focus!!");
      }
      // el && el.focus();
    },
    () => [ref.el]
  );
  // onMounted(() => {
  //   ref.el.focus();
  // });
  return ref;
}

// export { useAutoFocus };