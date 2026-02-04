import { createContext, useState } from "react";

export const CartContext = createContext();

export function CartProvider({ children }) {
  const [cart, setCart] = useState([]);

  const addItem = item => {
    setCart(prev => [...prev, item]);
  };

  const removeItem = id => {
    setCart(prev => prev.filter(i => i.id !== id));
  };

  const total = cart.reduce((sum, i) => sum + i.price, 0);

  return (
    <CartContext.Provider value={{ cart, addItem, removeItem, total }}>
      {children}
    </CartContext.Provider>
  );
                                  }
