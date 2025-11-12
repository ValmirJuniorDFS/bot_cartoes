@echo off
cd "C:\Users\transporte\Desktop\projeto cartão de natal"

echo ============================================
echo  🔄 ATUALIZANDO PROJETO NO GITHUB...
echo ============================================
git add .
git commit -m "atualização automática"
git push -u origin main

echo ============================================
echo  ✅ PROJETO ENVIADO COM SUCESSO!
echo ============================================
pause
