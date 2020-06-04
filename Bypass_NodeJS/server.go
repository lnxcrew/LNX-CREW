package main

import (
        "crypto/tls"
        "log"
        "net/http"
)

func HelloServer(w http.ResponseWriter, req *http.Request) {
        w.Write([]byte("This should not be displayed\n"))
}

func main() {
        http.HandleFunc("/hello", HelloServer)
        tlsConfig := &tls.Config{}

        server := &http.Server{
                Addr:      ":8444",
                TLSConfig: tlsConfig,
        }

        err := server.ListenAndServeTLS("cert.pem", "cert.key")
        if err != nil {
                log.Fatal("ListenAndServe: ", err)
        }
}