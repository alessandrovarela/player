#!/usr/bin/env python3
"""
Servidor HTTP simples para testar o player localmente
Uso: python3 server.py
Acesse: http://localhost:8000/test-player.html
"""

import http.server
import socketserver
import os
import sys

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adiciona headers CORS para evitar problemas
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Muda para o diretório do projeto
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor rodando em http://localhost:{PORT}")
        print(f"📱 Teste o player em: http://localhost:{PORT}/test-player.html")
        print("❌ Para parar: Ctrl+C")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✅ Servidor parado!")
            sys.exit(0)

if __name__ == "__main__":
    main()
