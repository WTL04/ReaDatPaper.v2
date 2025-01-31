"use client";
import { useEffect, useState } from "react";

export default function RootPage() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // fetching backend server
    fetch("http://localhost:8080/api/home")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // set data = data.message where message is from backend
        setMessage(data.message);
      });
  }, []);

  return (
    <>
      <div className="bg-blue-500 p-20">
        <h1>Home page</h1>
        <p> {message}</p>
        <input type="url" id="link" name="link" placeholder="Enter a link" />
      </div>
    </>
  );
}
