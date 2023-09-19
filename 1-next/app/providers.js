"use client";
import React, { useState, useEffect, createContext } from "react";
import { Progress } from "@nextui-org/react";
export const Context = createContext([]);

export function Providers({ children }) {
  const [user, setUser] = useState(null);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [routeText, setRouteText] = useState("Home");
  const [records, setRecords] = useState([]);
  const [userRecords, setUserRecords] = useState([]);
  const [categoryArr, setCategoryArr] = useState([]);
  const [userPrograms, setUserPrograms] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/currentUser", {
      method: "GET",
      credentials: "include",
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
        Accept: "application/json",
      },
    })
      .then((response) => (response.ok ? response.json() : null))
      .then((data) => {
        setUser(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error checking authentication:", error);
        setLoading(false);
      });
    fetch("http://127.0.0.1:5555/records", {
      credentials: "include",
    })
      .then((response) => (response.ok ? response.json() : null))
      .then((data) => {
        setRecords(data);
        setCategoryArr(data);
      })
      .catch((error) => console.error("Error fetching record data:", error));
  }, []);
  if (loading) {
    return (
      <div className="h-screen w-screen flex justify-center align-center items-center">
        <Progress
          size="md"
          isIndeterminate
          aria-label="Loading..."
          className="w-3/4 "
          color="success"
        />
      </div>
    );
  }
  return (
    <Context.Provider
      value={{
        userPrograms,
        setUserPrograms,
        loading,
        setLoading,
        userRecords,
        setUserRecords,
        routeText,
        setRouteText,
        isMenuOpen,
        setIsMenuOpen,
        records,
        setRecords,
        user,
        setUser,
        categoryArr,
        setCategoryArr,
      }}
    >
      {children}
    </Context.Provider>
  );
}
