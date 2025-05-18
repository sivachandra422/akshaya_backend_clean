from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import subprocess
from datetime import datetime

router = APIRouter(prefix="/forge")

class FullForgeRequest(BaseModel):
    app_name: str
    repo_url: str

@router.post("/full-cycle")
def forge_full_cycle(req: FullForgeRequest):
    app_name = req.app_name.strip().replace(" ", "_")
    repo_url = req.repo_url.strip()
    base_path = f"./generated/{app_name}"

    try:
        # STEP 1: Create project structure
        os.makedirs(f"{base_path}/lib/screens", exist_ok=True)

        with open(f"{base_path}/pubspec.yaml", "w") as f:
            f.write(f"name: {app_name}\nversion: 1.0.0+1\ndependencies:\n  flutter:\n    sdk: flutter")

        with open(f"{base_path}/lib/main.dart", "w") as f:
            f.write("""import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Akshaya Dream App',
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Akshaya Dream App')),
      body: Center(child: Text('Akshaya has generated this app.')),
    );
  }
}
""")

        with open(f"{base_path}/lib/screens/home.dart", "w") as f:
            f.write("// HomeScreen widget is defined in main.dart")

        # STEP 2: Push to GitHub
        if not os.path.exists(os.path.join(base_path, ".git")):
            subprocess.run(["git", "init"], cwd=base_path, check=True)
            subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=base_path, check=True)

        # Ensure git identity is set
        subprocess.run(["git", "config", "user.email", "akshaya@yourdomain.com"], cwd=base_path, check=True)
        subprocess.run(["git", "config", "user.name", "Akshaya Forge"], cwd=base_path, check=True)

        subprocess.run(["git", "add", "."], cwd=base_path, check=True)

        # Only commit if there are changes
        try:
            subprocess.run(["git", "commit", "-m", f"Akshaya Full-Cycle {datetime.utcnow().isoformat()}"], cwd=base_path, check=True)
        except subprocess.CalledProcessError as ce:
            raise HTTPException(status_code=400, detail="Nothing to commit. Repo might already be up to date.")

        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=base_path, check=True)

        return {
            "status": "success",
            "message": f"{app_name} generated and pushed to GitHub.",
            "timestamp": datetime.utcnow().isoformat(),
            "repo": repo_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))