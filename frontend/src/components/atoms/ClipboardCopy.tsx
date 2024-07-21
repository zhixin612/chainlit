import { useState } from 'react';
import { useCopyToClipboard } from 'usehooks-ts';

import IconButton, { IconButtonProps } from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';

import CopyIcon from 'assets/copy';

interface ClipboardCopyProps {
  value: string;
  theme?: 'dark' | 'light';
  edge?: IconButtonProps['edge'];
}

const ClipboardCopy: React.FC<ClipboardCopyProps> = ({ value, edge }) => {
  const [isCopied, setIsCopied] = useState(false);

  // use document.execCommand as fallback
  const handleCopy = () => {
    // create a temp element
    const tempInput = document.createElement('input');
    document.body.appendChild(tempInput);
    tempInput.value = value;
    tempInput.select();
    try {
      // try to copy
      const successful = document.execCommand('copy');
      if (successful) {
        setIsCopied(true);
      } else {
        throw new Error('Copy command failed');
      }
    } catch (err) {
      console.error('Failed to copy text: ', err);
    } finally {
      // delete the temp element
      document.body.removeChild(tempInput);
    }
  };

  const handleTooltipClose = () => {
    setIsCopied(false);
  };

  return (
    <Tooltip
      title={isCopied ? '复制成功！' : '复制'}
      onClose={handleTooltipClose}
      sx={{ zIndex: 2 }}
    >
      <IconButton color="inherit" edge={edge} onClick={handleCopy}>
        <CopyIcon sx={{ height: 16, width: 16 }} />
      </IconButton>
    </Tooltip>
  );
};

export { ClipboardCopy };
