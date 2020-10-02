import os
import json 
import time
path="/tmp/" #Path donde voy a guardar esto

backup_password='password'  #Password de origen 
restore_host="example.com" #DNS a donde voy a restorear
restore_user="admin" #Usuario con el que me voy a conectar para hacer el restore
restore_password="ABA_CA_BB" #Password destino
#en el origen ademas configuro a que base remota me voy a conectar para hacer el dump
origen=["bad.rds.1.com -d defaultdev",
        "bad.rds.2.com  -d defaultdev"
        ]
#en los backups, solo configuro a la base que me voy a conectar
backups=["database1",
         "database2"
  ]

def dump():
  for n in range(len(origen)):
      os.environ['PGPASSWORD'] = (backup_password)
      x= origen[n]    
      h= backups[n]
      
      dump="pg_dump -U postgres -h %s -f %s%s.sql"%(x,path,h) 
      print("\nDumping en %s en %s%s.sql\n"%(h,path,h))
      os.system(dump)
      print("####################################\nATR ese backup, ya quedo en en /tmp/%s.sql :P\n####################################"%(h))

def restore():
  for n in range(len(origen)):
    os.environ['PGPASSWORD'] = (restore_password)
    h= "%s.sql"%(backups[n])
    f= backups[n]
    
    restore="psql -h %s -d %s -U %s  < %s%s"%(restore_host,f,restore_user,path,h) 
    print("\nRestoring %s en %s\n"%(f,restore_host))
    os.system(restore)
    print("####################################\nListo Perri, ya quedo el restore ;) de %s\n####################################"%(f))
    os.system("sleep 8")

dump()
restore()
