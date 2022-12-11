import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { margin } from '@mui/system';

export default function ButtonAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" color="inherit">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            WAGER
          </Typography>
          {/* ログイン済みかどうかを判断して、結果によってヘッダに表示するボタンを変える */}
          {
            localStorage.getItem('token') ? <Button color="inherit" href="/" onClick={() => { localStorage.removeItem('token') }}>ログアウト</Button> :
              (
                <React.Fragment>
                  <Button color="inherit" href='/signin'>ログイン</Button>
                  <Button color="inherit" href='/signup'>アカウントを作成</Button>
                </React.Fragment>
              )
          }
        </Toolbar>
      </AppBar>
    </Box>
  );
}